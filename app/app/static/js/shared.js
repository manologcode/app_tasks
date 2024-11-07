function open_form_url_modal(url) {
    fetch(url)
      .then(data => {
        return data.text()
      })
      .then(data => {
        document.getElementById("sharedModal").innerHTML = data;
        openModal()
      })
  }

  function openModal(){
    document.getElementById('sharedModal').classList.remove('hidden');
  }

  function closeModal(){
    document.getElementById('sharedModal').classList.add('hidden');
  }


  function showConfirm(title, text, action){
    html = `
         <div class="bg-white p-6 rounded-lg shadow-lg w-80">
            <h3 class="text-lg font-semibold text-gray-800 mb-4">${title}</h3>
            <p class="text-gray-600 mb-6">¿Estás seguro de que deseas eliminar este proyecto?</p>
            <div class="flex justify-end space-x-4">
                <button onclick="toggleDeleteModal()" class="bg-gray-300 text-gray-700 px-4 py-2 rounded hover:bg-gray-400">Cancelar</button>
                <button onclick="confirmDelete({{ project.id if project else 'null' }})" class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-700">Eliminar</button>
            </div>
        </div>
    `
  }