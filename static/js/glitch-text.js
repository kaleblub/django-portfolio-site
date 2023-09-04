document.querySelectorAll(".glitch-text").forEach(button => {
    let interval;

    button.addEventListener("mouseover", event => {
        clearInterval(interval);

        const originalText = event.target.dataset.value;
        const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        const randomizedText = originalText
            .split("")
            .map(letter => letters[Math.floor(Math.random() * 26)])
            .join("");

        let iterations = 0;

        interval = setInterval(() => {
            const newText = originalText
                .split("")
                .map((letter, index) => {
                    if (index < iterations) {
                        return originalText[index];
                    }

                    return letters[Math.floor(Math.random() * 26)];
                })
                .join("");

            event.target.innerText = newText;

            if (iterations >= originalText.length) {
                clearInterval(interval);
                event.target.innerText = originalText;
            }

            iterations += 1 / 3;
        }, 30);
    });

    button.addEventListener("mouseout", event => {
        clearInterval(interval);
        event.target.innerText = event.target.dataset.value;
    });
});
