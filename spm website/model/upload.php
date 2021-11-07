<?php 
require_once "common.php";
session_start(); 
?>

<!DOCTYPE html>
<html lang="en" class='h-100'>
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
        
		<!-- BOOTSTRAP CSS -->
		<link rel="stylesheet" href="../css/bootstrap.min.css" />
        
		<!-- EXTERNAL CSS -->
        <link rel="stylesheet" href="../css/style.css" />

        <!-- Favicon -->
        <link rel="shortcut icon" type="image/jpg" href="../logo/favicon.ico"/>

        

	</head>


<?php

$uploaddao = new UploadDAO;
    $user = $_POST["submit"];
    if ($user=="link"){

        $form = array(
            "MaterialTitle" => $_POST["MaterialTitle"],
            "MaterialDescription" => $_POST["MaterialDescription"],
            "MaterialType" => $_POST["MaterialType"],
            "MaterialURL" => $_POST["MaterialURL"],
        );
     

    } else {
    
        $form = array(
            "MaterialTitle" => $_POST["MaterialTitle"],
            "MaterialDescription" => $_POST["MaterialDescription"],
            "MaterialType" => $_POST["MaterialType"],
            "file" => $_POST["MaterialURL"],
        );
       
} 

class material{

    private $MaterialTitle;
    private $MaterialDescription;
    private $MaterialType;
    private $MaterialURL;
    private $LessonID;

    public function __construct($MaterialTitle, $MaterialDescription, $MaterialType, $MaterialURL) {
      
        $this->MaterialTitle = $MaterialTitle;
        $this->MaterialDescription = $MaterialDescription;
        $this->MaterialType = $MaterialType;
        $this->MaterialURL = $MaterialURL;
        $this->LessonID = $LessonID;

    } 

    public function getMaterialTitle(){
        return $this->MaterialTitle;
    }

    public function getMaterialDescription(){
        return $this->MaterialDescription;
    }

    public function getMaterialType(){
        return $this->MaterialType;
    }

    public function getMaterialURL(){
        return $this->MaterialURL;
    }

    public function getLessonID(){
        return $this->LessonID;
    }


    public function setLessonID($LessonID){
        $this->LessonID;
    }
    

    public function setMaterialTitle($MaterialTitle){
        $this->email;
    }
  
    public function MaterialDescription($MaterialDescription){
        $this->MaterialDescription;
    }

    public function setMaterialType($MaterialType){
        $this->postal;
    }

    public function setMaterialURL($MaterialURL){
        $this->MaterialURL;
    }

}

?>



<!-- BOOTSTRAP JS -->
<script src="../js/jquery-3.5.1.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>

