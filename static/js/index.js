


let hbtn = document.querySelector('.header__row-mobile');
let header__wrappers = document.querySelector('.header__wrappers')

// https://codepen.io/noirsociety/pen/ZEwLGXB
document.querySelector("#clickModal").addEventListener('click', () => {
  document.body.classList.add('activaModal')
  document.querySelector('#closeModal').addEventListener('click', () => {
    document.body.classList.remove('activaModal')
  })
})

function queryElement(el, state) {
  document.querySelector(el).style.display = state
}

hbtn.addEventListener('click', function (e) {
  header__wrappers.classList.toggle('mobil_app')
  if (header__wrappers.classList.contains('mobil_app')) {
    queryElement('.end_clock', 'none');
    queryElement('.click_look', 'block');
  } else {
    queryElement('.end_clock', 'block');
    queryElement('.click_look', 'none');
  }

})

if (localStorage.theme == 1) {
  document.body.classList.add('dark')
  document.querySelector('.ball').style.transform = 'translateY(24px)'
}


document.querySelector('#chk').addEventListener('click', () => {
  if (localStorage.theme == null || localStorage.theme == 0) {
    document.body.classList.add('dark')
    document.querySelector('.ball').style.transform = 'translateY(24px)'
    localStorage.theme = 1
  } else if (localStorage.theme == 1) {
    document.body.classList.remove('dark')
    document.querySelector('.ball').style.transform = 'translateY(0px)'
    localStorage.theme = 0
  }
});




function resElemen(el, name) {
  if (el.querySelector(name).style.opacity == 0) {
    el.querySelector(name).style.opacity = 1
    el.querySelector(name).style.height = 'auto'
    el.querySelector('.answers__item-bottom p').style.marginTop = '15px'
    el.querySelector('.down-answers__item').style.display = 'none'
    el.querySelector('.know-answers__item').style.display = 'block'
    return
  }
  el.querySelector(name).style.opacity = 0
  el.querySelector(name).style.height = '0px'
  el.querySelector('.answers__item-bottom p').style.marginTop = '0px'
  el.querySelector('.down-answers__item').style.display = 'block'
  el.querySelector('.know-answers__item').style.display = 'none'
}



const answers__item = document.querySelectorAll('.answers__item')
for (let i = 0; i < answers__item.length; i++) {
  answers__item[i].addEventListener('click', (e) => {
    resElemen(answers__item[i], '.answers__item-bottom')
  })

}