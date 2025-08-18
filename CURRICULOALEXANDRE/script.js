window.onload = function() {
    const canvas = document.getElementById("grafico");
    if (canvas.getContext) {
        const ctx = canvas.getContext("2d");
        ctx.fillStyle = "#009688";
        ctx.fillRect(10, 10, 200, 50);
    }
};
