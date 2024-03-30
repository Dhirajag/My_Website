


ScrollReveal({ 
   reset: true ,
    distance:'80px',
    duration:2000,
    delay:200
});
ScrollReveal().reveal('.about-content', { origin:'top' });
ScrollReveal().reveal('.about-img', { origin:'bottom' });
ScrollReveal().reveal('.about-content h1', { origin:'left' });
ScrollReveal().reveal('.home-content p', { origin:'right' });



const typed = new Typed('.multiple,heading', {
strings: ['Frontend Developer','Designer'],
typeSpeed:70,
backSpeed:70,
backDelay:1000,
loop:true
});
