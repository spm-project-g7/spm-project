async function addMaterial() {
    // console.log("hello");
    var LessonID = $('#LessonID').val();
    var serviceURL = "http://127.0.0.1:8000/api/v1/material/" + LessonID
    var MaterialID = $('#name').val();
    
    console.log(JSON.stringify({ LessonID: LessonID, MaterialID: MaterialID }));
    try {
        const response =
        await fetch(
            serviceURL, {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ LessonID: LessonID, MaterialID: MaterialID})
        });
        const data = await response.json();
        const information = await data;
        // console.log(information);
        if(response.ok){
            alert("Upload Success!");
            window.location.replace("course.html");
        } else {
            alert(data.message);
        }
        
    }
    catch (error) {
        // Errors when calling the service; such as network error, 
        // service offline, etc
        console.log(error);
        alert('There is a problem uploading material, please try again later.');
    } // error

};
