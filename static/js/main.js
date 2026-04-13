document.addEventListener("DOMContentLoaded", function() {
    let c = document.querySelectorAll('.card');
    c.forEach(function(e) {
        e.classList.add('anim');
        e.addEventListener('mouseenter', function() {
            this.style.boxShadow = "0 10px 20px rgba(242, 116, 39, 0.15)";
            this.style.transform = "translateY(-5px)";
        });
        e.addEventListener('mouseleave', function() {
            this.style.boxShadow = "0 0.125rem 0.25rem rgba(0, 0, 0, 0.075)";
            this.style.transform = "translateY(0)";
        });
    });

    let b = document.querySelectorAll('.btn');
    b.forEach(function(x) {
        x.classList.add('anim');
        x.addEventListener('mousedown', function() {
            this.style.transform = "scale(0.95)";
        });
        x.addEventListener('mouseup', function() {
            this.style.transform = "scale(1)";
        });
    });
});
