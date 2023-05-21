const paragraphBox = document.getElementById("paragraph-box");
const paragraphContent = document.getElementById("paragraph-content");

// Change the border color of the box when the mouse hovers over it
paragraphBox.addEventListener("mouseover", function() {
  paragraphBox.style.borderColor = "red";
});

// Change the border color of the box back to black when the mouse leaves the box
paragraphBox.addEventListener("mouseout", function() {
  paragraphBox.style.borderColor = "black";
});

// Change the font size of the paragraph when the box is clicked
paragraphBox.addEventListener("click", function() {
  paragraphContent.style.fontSize = "20px";
});
