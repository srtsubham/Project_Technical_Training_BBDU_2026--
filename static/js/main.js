document.addEventListener("DOMContentLoaded", function() {
    let interfaceCards = document.querySelectorAll('.card');
    interfaceCards.forEach(function(currentCard) {
        currentCard.style.transition = "all 0.3s ease";
        currentCard.addEventListener('mouseenter', function() {
            this.style.boxShadow = "inset 0 1px 1px rgba(255,255,255,0.1), 0 15px 30px rgba(255, 59, 59, 0.15)";
            this.style.transform = "translateY(-5px)";
        });
        currentCard.addEventListener('mouseleave', function() {
            this.style.boxShadow = "inset 0 1px 1px rgba(255,255,255,0.05), 0 8px 20px rgba(0, 0, 0, 0.9)";
            this.style.transform = "translateY(0)";
        });
    });

    let scrollContainer = document.getElementById("scrollTypingContainer");
    let targetHeading = document.getElementById("dynamicTextTarget");
    let navigationMenu = document.getElementById("navigationBar");
    let backgroundGrid = document.getElementById("scrollBg");
    let medicalCross = document.getElementById("medicalCross");
    let flareNode = document.getElementById("flareNode");
    let mottoPhrase = "ELEVATING THE STANDARD OF MODERN HEALTHCARE";

    if (scrollContainer && targetHeading) {
        window.addEventListener("scroll", function() {
            let containerBounds = scrollContainer.getBoundingClientRect();
            let screenHeight = window.innerHeight;

            if (containerBounds.top <= 0 && containerBounds.bottom >= screenHeight) {
                if (navigationMenu) navigationMenu.style.transform = "translateY(-100%)";

                let scrollDistance = containerBounds.height - screenHeight;
                let pixelsScrolled = Math.abs(containerBounds.top);
                let scrollPercentage = pixelsScrolled / scrollDistance;

                if (scrollPercentage < 0) scrollPercentage = 0;
                if (scrollPercentage > 1) scrollPercentage = 1;

                let visibleCharacters = Math.floor(scrollPercentage * mottoPhrase.length);
                targetHeading.textContent = mottoPhrase.substring(0, visibleCharacters);

                // Grid Fade In
                if (backgroundGrid) {
                    backgroundGrid.style.opacity = (scrollPercentage).toString();
                }

                // Cross Expand and Fade In
                if (medicalCross) {
                    let expansionScale = 0.5 + (scrollPercentage * 0.7);
                    medicalCross.style.opacity = scrollPercentage.toString();
                    medicalCross.style.transform = `translate(-50%, -50%) scale(${expansionScale})`;
                }

                // Flare Ignite
                if (flareNode) {
                    let flareScale = 0.5 + (scrollPercentage * 1.2);
                    flareNode.style.opacity = scrollPercentage.toString();
                    flareNode.style.transform = `translate(-50%, -50%) scale(${flareScale})`;
                }

            } else {
                if (navigationMenu) navigationMenu.style.transform = "translateY(0)";

                if (containerBounds.bottom < screenHeight) {
                    targetHeading.textContent = mottoPhrase;
                    if (backgroundGrid) backgroundGrid.style.opacity = "1";
                    if (medicalCross) {
                        medicalCross.style.opacity = "1";
                        medicalCross.style.transform = "translate(-50%, -50%) scale(1.2)";
                    }
                    if (flareNode) {
                        flareNode.style.opacity = "1";
                        flareNode.style.transform = "translate(-50%, -50%) scale(1.7)";
                    }
                } else if (containerBounds.top > 0) {
                    targetHeading.textContent = "";
                    if (backgroundGrid) backgroundGrid.style.opacity = "0";
                    if (medicalCross) {
                        medicalCross.style.opacity = "0";
                        medicalCross.style.transform = "translate(-50%, -50%) scale(0.5)";
                    }
                    if (flareNode) {
                        flareNode.style.opacity = "0";
                        flareNode.style.transform = "translate(-50%, -50%) scale(0.5)";
                    }
                }
            }
        });
    }
});
