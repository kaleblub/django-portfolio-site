//--------- Get All The Elements With The Class 'nav-link' ---------//
const navItems = document.getElementsByClassName('nav-link');


// ---------- REQUIREMENTS/PSEUDO CODE ----------- // 
// - IF {CURRENT_PAGE} IS THE 'nav-link' being hovered
//      - THEN don't type anything out
// - IF HOME is hovered,
//      - TYPE OUT 'cd ~'  
//
// - ON THE ABOUT PAGE
//      - IF THE 'cv-btn' is hovered
//          - TYPE OUT "cat Kaleb.Resume.pdf"
//      - IF THE Contact 'nav-link' is hovered,
//          - TYPE OUT "python3 contactKaleb.py"

function typeOutChosenText(element, enterText, exitText) {
    element.addEventListener('mouseover', () => {
        document.getElementById('typedText').textContent = enterText;
    });
    element.addEventListener('mouseleave', () => {
        document.getElementById('typedText').textContent = exitText;
    });
}


for(var i = 0; i < navItems.length; i++) {
    let currentItem = navItems[i];
    let text = currentItem.innerHTML;
    
    if(text.toLowerCase() == 'home') {
        typeOutChosenText(currentItem, 'cd ~', '');
    } else if(text.toLowerCase() == 'contact') {
        typeOutChosenText(currentItem, 'python3 contactKaleb.py', '');
    } else {
        typeOutChosenText(currentItem, 'cd /' + text, '');
    }
}

