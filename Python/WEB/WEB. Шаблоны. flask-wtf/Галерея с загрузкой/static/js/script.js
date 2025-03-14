document.getElementById('upload_image_form').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const fileInput = document.getElementById('file');
    const file = fileInput.files[0]; 

    if (file) {
        const fileName = file.name; 
        document.getElementById('result').innerText = "Название загруженного файла: " + fileName; 
    } else {
        document.getElementById('result').innerText = "Файл не выбран.";
    }
});