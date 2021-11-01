const clientsDataBox = document.getElementById('clients_list')
$.ajax({
    type: 'GET',
    url: '/applications/clients-json/',
    success: function (c_response) {
        const clientsData  = c_response.data
        console.log(c_response.data)
        clientsData.map(client=>{
            const option = document.createElement('option')
            option.textContent = client.client_name
            option.setAttribute('data-value',client.id)
            option.setAttribute('value',client.client_name)
            option.setAttribute('label',client.client_name)
            clientsDataBox.appendChild(option)
        })
    },
    error: function (error) {
        console.log(error)
    }
})

document.querySelector('input[list]').addEventListener('input', function(e) {
            var input = e.target,
                list = input.getAttribute('list'),
                options = document.querySelectorAll('#' + list + ' option'),
                hiddenInput = document.getElementById(input.getAttribute('id') + '-hidden'),
                label = input.value;
            hiddenInput.value = label;
            for(var i = 0; i < options.length; i++) {
                var option = options[i];
                if(option.innerText === label) {
                    hiddenInput.value = option.getAttribute('data-value');
                    break;
                }
            }

        });

const clientInput = document.getElementById('id_client')

clientInput.addEventListener('change', e=>{
    const selectedClient = e.target.value
    const clients_addressDataBox = document.getElementById('id_client_address')
    clients_addressDataBox.innerHTML = ''
    $.ajax({
        type: 'GET',
        url: `/applications/client_address-json/${selectedClient}`,
        success: function (ca_response) {
            const clientsPersonsData  = ca_response.data
            clientsPersonsData.map(client_address=>{
                const option = document.createElement('option')
                option.textContent = client_address.address
                option.setAttribute('data_value',client_address.address)
                option.setAttribute('value',client_address.id)
                clients_addressDataBox.appendChild(option)
            })
        },
        error: function (error) {
            console.log(error)
        }
    })

    const clients_personDataBox = document.getElementById('id_client_person')
    clients_personDataBox.innerHTML = ''
    $.ajax({
        type: 'GET',
        url: `/applications/clients_person-json/${selectedClient}`,
        success: function (cp_response) {
            const clientsPersonsData  = cp_response.data
            clientsPersonsData.map(client_person=>{
                const option = document.createElement('option')
                option.textContent = client_person.client_person_name
                option.setAttribute('value',client_person.id)
                option.setAttribute('data_value',client_person.client_id)
                clients_personDataBox.appendChild(option)
            })
        },
        error: function (error) {
            console.log(error)
        }
    })
})

