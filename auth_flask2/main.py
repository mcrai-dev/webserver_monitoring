# Pour les itinéraires, vous utiliserez deux plans.

# Pour le, vous aurez une page d’accueil () et une page de profil ().main_blueprint//profile
from flask import Flask, Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Log, Command, Device
import datetime as dt
import time
import random
from . import ping
from wakeonlan import send_magic_packet
from . import wol
from . import serial_cnx
from . import cpuChecker
from . import cpuTemperature
# import RPi.GPIO as GPIO
# from time import sleep
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        if request.form['code'] == 'ip_check':
            ip_Address = request.form['ip_Address']
            output = ip_Address
            if ip_Address:
                print(f'the IP Address is {output}')
                result_ping = ping.ping(output)
                print(f"the PING RESULT {result_ping}")
                # check the result of ping
                if "4 received" in str(result_ping):
                    print(f'the IP Address is =====================connected 2')
                    return jsonify({'out': ' Connected.'})
                elif "reçus = 4" in str(result_ping):
                    print(f'the IP Address is =====================connected 3')
                    return jsonify({'out': ' Connected.'})
                else:
                    print(f'the IP Address is =====================NOT connected')
                    return jsonify({'out': ' not connected.'})
            return jsonify({'error': 'error !'})

        elif request.form['code'] == 'timeBrut':
            timeBrut = request.form['timeBrut']
            output = timeBrut

            # registre the active command in database
            command = Command(
                rebour=timeBrut, name_commander=current_user.name)
            db.session.add(command)
            db.session.flush()
            db.session.commit()
            # format is 'MMM dd, YYYY HH:MM:SS' example Nov 02, 2022 12:05:55
            #print(f'the timestamp from calendar is {timeBrut}')
            timeis = timeBrut[len(timeBrut)-8: len(timeBrut)]

        # get the time
            #print(f'time: {timeis}')
            tab_time = timeis.split(":")
            time_splitted = []
            #print(f'the tab_time is = {tab_time}')
            for w in tab_time:
                if any(c.isdigit() for c in w):
                    time_splitted.append(w)
            #print(f'the time_splitted[0]={time_splitted[0]}\nthe time_splitted[1]={time_splitted[1]}\nthe time_splitted[2]={time_splitted[2]}\n')

        # get the year and month and day
            dateis = timeBrut[0: len(timeBrut)-9]
            #print(f'datis = {dateis}')
            tab_date = dateis.split(" ")
            date_splitted = []
            for y in tab_date:
                if any(d.isalnum() for d in y):
                    date_splitted.append(y)
            #print(f'the date_splitted[0]={date_splitted[0]}\nthe date_splitted[1]={date_splitted[1]}\n the date_splitted[2]={date_splitted[2]}\n')
            date_splitted_1_virgule = date_splitted[1]
            date_splitted_1_remove_virgule = date_splitted_1_virgule[0:len(
                date_splitted_1_virgule)-1]
            #print(f'the date_splitted[0]={date_splitted[0]}\nthe date_splitted[1]={date_splitted[1]}\n the date_splitted[2]={date_splitted[2]}\n')

        # activate the countdown
        # Hour = time_splitted[0]       month = date_splitted[0]
        # min  = time_splitted[1]       Day   = date_splitted[1] = date_splitted_1_remove_virgule
        # sec  = time_splitted[2]       Year  = date_splitted[2]
        # chooseDate(yyyy, MM, dd, hh, min, ss):
            end = chooseDate(date_splitted[2], date_splitted[0], date_splitted_1_remove_virgule,
                             time_splitted[0], time_splitted[1], time_splitted[2])
            # countdown(end)
            while True:
                difference = end - dt.datetime.now()
                count_hours, rem = divmod(difference.seconds, 3600)
                count_minutes, count_seconds = divmod(rem, 60)
                if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
                    print("time is up!")
                    break

            #print('the count is: ' + str(difference.days) + " D, " + str(count_hours) + " H:" + str(count_minutes) + " M:" + str(count_seconds) + " S")
            count = str(difference.days) + " D, " + str(
                count_hours) + " H:" + str(count_minutes) + " M:" + str(count_seconds) + " S"
            time.sleep(1)
            return jsonify({'count': ' ' + count + 'Connected.'})

        # to turn on the target
        elif request.form['code'] == 'toggle':
            #print(f'it is toggle')
            turn = request.form['keywords']
            device_id = request.form['cible']
            device_to_command = Device.query.filter_by(id=device_id).first()
            #print(f'the keywords is {turn}')
            if device_to_command and turn == 'turn_on':
                #print(f'the cible ID  is {device_id}')
                #print(f'the cible MAC  is {device_to_command.mac_address} TURN ON')
                activity = turn
                activity_time = request.form['time']
                name = current_user.name
                log = Log(time=activity_time, name=name, activity=activity)
                db.session.add(log)
                db.session.commit()
                #send_magic_packet(macs= str(device_to_command.mac_address), ip_Address="192.168.0.2", interface="192.168.0.1")
                wol.create_wol_packet(device_to_command.mac_address)
                return jsonify({'next_state': 'Turn OFF the target'})
            elif device_to_command and turn == 'turn_off':
                #print(f'the cible ID  is {device_id}')
                #print( f'the cible MAC  is {device_to_command.mac_address} TURN Off')
                activity = turn
                activity_time = request.form['time']
                name = current_user.name
                log = Log(time=activity_time, name=name, activity=activity)
                db.session.add(log)
                db.session.commit()
                return jsonify({'next_state': 'Turn ON the target'})

        # this one is turn in loop to send the data from capter to UI
        elif request.form['code'] == 'data_plot':
            key = request.form['keywords']
            #print(f'tdata plot {key}')
            cpu = cpuChecker.get_cpu_percent()
            temperature = round(cpuTemperature.getCPUTemperature(),1)
            data =serial_cnx.sendRequestVoltage()
            data2 = round(random.uniform(1.08, 1.99),2)
            # GPIO.output(8, GPIO.HIGH)
            # sleep(1)
            # GPIO.output(8, GPIO.LOW)
            # sleep(0.5)
            objet = Command.query.all()
            rebour = str(objet[-1].rebour)
            #print(f'the data  is {data}')
            return jsonify({'data_bute': str(data)+'#'+str(data2)+'#'+str(rebour)+'#'+str(cpu)+'#'+str(temperature)})

        # get the data in add device
        elif request.form['code'] == 'add_device':
            device_name = request.form['device_name']
            device_mac = request.form['device_mac']
            db.session.add(Device(name=device_name, mac_address=device_mac))
            db.session.flush()
            db.session.commit()
            obj = Device.query.all()
            id_last = str(obj[-1].id)
            name_last = str(obj[-1].name)
            mac_last = str(obj[-1].mac_address)
            return jsonify({'status': id_last+' - '+name_last+' '+mac_last})

            # fetch all the data in add device
        # elif request.form['code'] == 'fetch_device':
        #     db.session.add(Device(name=device_name, mac_address = device_mac))
        #     return jsonify({'status':'success'})

        return jsonify({'error': 'error !'})
    all_device = Device.query.all()
    #print(all_device)
    return render_template('profile.html', name=current_user.name, device=Device.query.all())
    # return render_template('profile.html', name=current_user.name)

# function coose date use for getting the date


def chooseDate(yyyy, MM, dd, hh, min, ss):
    tab = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    end_time = dt.datetime(int(yyyy), int(
        tab.index(MM)) + 1, int(dd), int(hh), int(min), int(ss))
    #print(f"index choosen is{int(tab.index(MM)) +1}")
    #print(f'YYYY= {yyyy} month = {int(tab.index(MM)) +1} day = {dd} hour={hh} min = {min} sec = {ss}')
    return end_time
