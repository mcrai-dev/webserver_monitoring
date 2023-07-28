// this function fetch data on database and show on field.
function getDeviceData() {
    // Envoi d'une requête AJAX pour obtenir les données de la table "Device"
    $.ajax({
      url: '/profile',
      type: 'GET',
      success: function(data) {
        // Réinitialiser la liste
        $('#liste').empty();
       
        // Boucler sur les données reçues et ajouter des éléments <li> à la liste
    //     <li class="list-group-item list-group-item-action" >
    //     <div class="device" >
    //         <p><i class="fa-solid fa-server"></i> <b>{{device.id}}</b> - {{device.name}} {{device.mac_address}} </p>
    //     </div>
    // </li>

        // for (let i = 0; i < data.length; i++) {
        //   let device = data[i];
        //   console.log('------------------')
        //   console.log(device)
        //   let li = $('<li >').text(device.id + ' - ' + device.name + ' - ' + device.mac_address);
        //   $('#liste').append(li);
        // }
      }
    });
  }
  
  // Appeler la fonction pour obtenir les données initiales
//   getDeviceData();
  
//   // Définir un intervalle pour mettre à jour les données en temps réel
//   setInterval(getDeviceData, 1000); // toutes les 1 secondes
  

function add_new_device() {
    if ($("#device_name").val() === "" || $("#device_mac").val() === "") {
        alert("le champs est vide")
    } else {
        executeAsync(function () {
            $.ajax({
                data: {
                    code: "add_device",
                    device_name: $('#device_name').val(),
                    device_mac: $('#device_mac').val(),
                },
                type: 'POST',
                url: '/profile'
            }).done(function (data) {
                $('#device_name').val('')
                $('#device_mac').val('')
                // newDeviceAdd =
                //     '<div id="row"> <div class="input-group m-3">' +
                //     '<div class="input-group-prepend">' +
                //     '<button class="btn btn-danger" id="DeleteRow" type="button">' +
                //     '<i class="bi bi-trash"></i> Delete</button> </div>' +
                //     '<input type="text" class="form-control m-input"> </div> </div>';
                newDeviceAdd = '<li class="list-group-item list-group-item-action" >' +
                    ' <div class="device" >' +
                    ' <p><i class="fa-solid fa-server"></i> ' + data.status + '</p>' +
                    ' </div> ' +
                    ' </li>';
                $('#liste').append(newDeviceAdd)
                value_id_of_device = data.status.split(' -')
                newSelectedDevice =  '<option value='+value_id_of_device+'>'+data.status+'</option>'
                $('#device_form').append(newSelectedDevice)


            });
        });
    }
}
