//
// let addSession = document.getElementsByClassName ('addSession')
// if(addSession) {
//     addSession.forEach(sessionClass => {
//         console.log(sessionClass)
//         sessionClass.addEventListener('change', (evt) => {
//             evt.currentTarget
//                 .querySelectorAll('.activeType')
//                 .forEach(element => {
//                     element.classList.remove("activeType")
//                 })
//
//             evt.target
//                 .closest('.count_icon')
//                 .classList.add("activeType");
//         }, true);
//     })
// }
//

const chooseFile = (evt) => {
    document.querySelector('.imageInput').click()
}

const hoverCircle = () =>{
    let imgCircle = document.querySelector('.imgCircle')
    let circleOnHover = document.querySelector('.circleOnHover')
    imgCircle.addEventListener('mouseover', (evt) =>{
        circleOnHover.classList.add('onHoverfilter')

    })

    imgCircle.addEventListener("mouseleave", (evt) => {
        circleOnHover.classList.remove('onHoverfilter')
  });
}
const messageSuccess = () =>{
      let savedWrap = document.querySelector('.savedWrap')
    if (savedWrap){
        setTimeout(fade_out, 3000);
    function fade_out() {
        savedWrap.remove()
    }

    }
}



allFunctions()
if (document.readyState !== 'loading') {
    allFunctions()
}

document.body.addEventListener('htmx:afterOnLoad', event=>{
    allFunctions()
})


function allFunctions(){

    hoverCircle()
    messageSuccess()
}