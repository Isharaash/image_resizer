const widthInput = document.getElementById('width');
const heightInput = document.getElementById('height');
const aspectRatioCheckbox = document.getElementById('aspectRatio');
let originalWidth, originalHeight, aspectRatio;

document.getElementById('image').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
        const img = new Image();
        img.onload = function () {
            originalWidth = img.width;
            originalHeight = img.height;
            aspectRatio = originalWidth / originalHeight;

            // Set initial values in the input fields
            widthInput.value = originalWidth;
            heightInput.value = originalHeight;
        };
        img.src = URL.createObjectURL(file);
    }
});

// Event listener for width input
widthInput.addEventListener('input', function () {
    if (aspectRatioCheckbox.checked && aspectRatio) {
        heightInput.value = Math.round(widthInput.value / aspectRatio);
    }
});

// Event listener for height input
heightInput.addEventListener('input', function () {
    if (aspectRatioCheckbox.checked && aspectRatio) {
        widthInput.value = Math.round(heightInput.value * aspectRatio);
    }
});
