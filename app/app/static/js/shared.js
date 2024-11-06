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
