// Dropdown Sidebar Menu
let sidebarItems = document.querySelectorAll('.sidebar-item.has-sub');
for(var i = 0; i < sidebarItems.length; i++) {
    let sidebarItem = sidebarItems[i];
	sidebarItems[i].querySelector('.sidebar-link').addEventListener('click', function(e) {
        e.preventDefault();
        
        let submenu = sidebarItem.querySelector('.submenu');

        if(submenu.classList.contains('active')) submenu.classList.remove('active');
        else submenu.classList.add('active');
    })
}

// Navbar Toggler
let sidebarToggler = document.querySelectorAll(".sidebar-toggler");
for (var i = 0; i < sidebarToggler.length; i++) {
    let toggler = sidebarToggler[i];
    toggler.addEventListener('click', () => {
        let sidebar = document.getElementById('sidebar');
        if(sidebar.classList.contains('active')) sidebar.classList.remove('active');
        else sidebar.classList.add('active');
    });
}

// Perfect Scrollbar INit
if(typeof PerfectScrollbar == 'function') {
    const container = document.querySelector(".sidebar-wrapper");
    const ps = new PerfectScrollbar(container);
}

window.onload = function() {

    var w = window.innerWidth;
    if(w < 768) {
        console.log('widthnya ', w)
        document.getElementById('sidebar').classList.remove('active');
    }
}

// feather.replace();

// my functions
var modal = new bootstrap.Modal(document.getElementById('modal-default'));
document.getElementById("change-pass").addEventListener("click", modal_change_pass);
document.getElementById("edit-my-user").addEventListener("click", modal_change_data);

function modal_change_pass() {
  let url = '/main/change_pass'
  open_form_url_modal(url)
} 

if (document.querySelector('[data-confirm]')){
  const link_confirm = document.querySelectorAll('[data-confirm]');
  for (let i = 0; i < link_confirm.length; i++) {
    link_confirm[i].addEventListener('click', show_form_confirm)
  }
}

function select_change_options_list(id_sel, data){
  selectBox = document.getElementById(id_sel)
  while (selectBox.length > 0) {
    selectBox.remove(0);
  }
  // selectBox.appendChild(create_option('',"-----------------"))
  // console.log(data)
  for (const item of data) {
    selectBox.appendChild(create_option(item[0],item[1]));
  }
}

function select_change_options(id_sel, data){
  selectBox = document.getElementById(id_sel)
  while (selectBox.length > 0) {
    selectBox.remove(0);
  }
  selectBox.appendChild(create_option('',"-----------------"))
  for (let key in data) {
    selectBox.appendChild(create_option(key,data[key]));
  }
}

function create_option(id,text){
  let option = document.createElement("option");
  option.setAttribute('value', id);
  let optionText = document.createTextNode(text);
  option.appendChild(optionText);
  return option
}

function modal_change_data() {
  let url = '/users/change_data'
  open_form_url_modal(url)
}   

  function open_form_url_modal(url) {
    fetch(url)
      .then(data => {
        return data.text()
      })
      .then(data => {
        document.getElementById("modal_content").innerHTML = data;
        modal.show();
        if (document.getElementById('btn-submit')){
          document.getElementById('btn-submit').addEventListener('click', send_form)
        }
        if (document.querySelector('[data-confirm]')){
          const link_confirm = document.querySelectorAll('[data-confirm]');
          for (let i = 0; i < link_confirm.length; i++) {
            link_confirm[i].addEventListener('click', show_form_confirm)
          }
        }
      })
  }



  function show_form_confirm(){
    show_modal_confirm(this)
  }

  function show_modal_confirm(self){
    url = self.dataset.url;

    window.event.preventDefault();
    message = self.getAttribute('data-confirm')
    document.getElementById('content-confirm').innerHTML = message
    var modal_confirm = new bootstrap.Modal(document.getElementById('modal-confirm'));
    modal_confirm.show();
    document.getElementById('confirm_confirm').addEventListener('click', ()=>{ 
      if (self.hasAttribute('data-ajax')) {
        modal_confirm.hide();
        open_form_url_modal(url)
      }else{
        window.location.href = url
      }
    })
    document.getElementById('confirm_cancel').addEventListener('click', ()=>{ modal_confirm.hide();})
  }


  function send_form(){
      let form = document.getElementById('form')
      let url = form.getAttribute("action")
      
      if (!form.checkValidity()) {
       console.log("passss")
       first_field = form.querySelectorAll(':invalid')[0]
       first_field.reportValidity()
       first_field.focus()
       return false
      }
      const data = new FormData(form)
      fetch(url, {
      method: 'POST',
      body: data
      })
      .then(async response => {
        const contentType = response.headers.get("content-type");
        if (contentType && contentType.indexOf("application/json") !== -1) {
          const data = await response.json();
          if (data.reload == 'true') {
            location.reload();
          } else {
            if (data.tag) {
              cleanurl = window.location.href.split('?')[0].replace('#','')
              new_url = cleanurl + "?tag=" + data.tag
              history.pushState(null, ' ', new_url); 
              location.reload()
            }else{
              open_alert(data);
            }
          }
        } else {
          const html = await response.text();
          document.getElementById('modal_content').innerHTML = html;
        }
      })
   }

    function send_form_not_response(){
      let form = document.getElementById('form')
      let url = form.getAttribute("action")
      const data = new FormData(form)
      fetch(url, {
      method: 'POST',
      body: data
      })
    }


   function update_one_field(){

    let field_name = this.name
    if (this.getAttribute('type') === 'checkbox'){
      field_val = this.checked || false
    }else{
      field_val = this.value
    }

    const currert_url = window.location.href
    const urlp = currert_url.split('/')
    url = urlp[0] + '//' + urlp[2] + '/' + urlp[3] + '/up_field/' + urlp[5]
    
    const data =  JSON.stringify({name: field_name, value: field_val})
    sendPostJson(url,data)
 }

 function render_partial(url,data,id_html){
  fetch(url, {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
  })
    .then((response) => {
    return response.text();
  })
  .then(function(html) {
    document.getElementById(id_html).innerHTML= html
  })
  .catch(function(err) {
  console.log(err);
  });
}


 function sendPostJson(url,data){
    fetch(url, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: data 
    })
    .then(function(response) {
      console.log(response)
      if(response.ok) {
        return response.json()
      } else {
          throw "Error en la llamada Ajax";
      }
    })
    .then(function(message) {
        open_alert(message)
    })
    .catch(function(err) {
    console.log(err);
    });
 }

  function load_url(url, id_element) {
    fetch('url')
      .then(data => {
        return data.text()
      })
      .then(data => {
        document.getElementById(id_element).innerHTML = data;
      })
  }

  function validatePass() {
    pass1 = document.getElementById('password');
    pass2 = document.getElementById('password1');
    console.log(`${pass1.value} != ${pass2.value}`)
    if (pass1.value != pass2.value) {
      alert("las contraseñas no coinciden")
      e.preventDefault();
      return false;
    }else{
      document.forms['passform'].submit();
    }
  }

  async function getCurrenIp (){
    const url = 'https://api.my-ip.io/ip'
    const response = await fetch(url)
    const data = await response.text() 
    return data
  }

  async function isPossibleSing(ip) {
    try {
      current= await getCurrenIp()
    } catch (error) {
      current='errorConex'
    }
    console.log(current)
    const hour_input=document.getElementById('hour-input')
    const hour_message=document.getElementById('hour-message')
    if( current == 'errorConex' || '' == ip || current.ip == ip){
      hour_input.classList.remove("hide")
    }else{
      if (hour_message)
        hour_message.classList.remove("hide")
    }
  }

  function printUrl(url){
    fetch(url).then(data => {  return data.text() }).then(data => {
      var ventana = window.open('', 'PRINT', 'height=600,width=800');
      ventana.document.write('<html><head><title>Print</title>');
      ventana.document.write('<link rel="stylesheet" href="/static/css/bootstrap.css">');
      ventana.document.write('<link rel="stylesheet" href="/static/css/print-format.css">');
      ventana.document.write('</head><body>');
      ventana.document.write(data);
      ventana.document.write('</body></html>');
      ventana.document.close();
      ventana.focus();
      ventana.onload = function() {
        ventana.print();
        ventana.close();
      };
    })
  }


  function printDiv(div) {
    elemento = document.getElementById(div)
    var ventana = window.open('', 'PRINT', 'height=600,width=800');
    ventana.document.write('<html><head><title>' + document.title + '</title>');
    ventana.document.write('<link rel="stylesheet" href="/static/css/print.css">');
    ventana.document.write('</head><body >');
    ventana.document.write(elemento.innerHTML);
    ventana.document.write('</body></html>');
    ventana.document.close();
    ventana.focus();
    ventana.onload = function() {
      ventana.print();
      ventana.close();
    };
    return true;
  }