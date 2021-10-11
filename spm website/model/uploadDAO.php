<?php

/* Functions:
signup ($form) --> TRUE/FALSE
retrieveUser($email) --> User(email, password, name)
isExistingUser($email) --> TRUE/FALSE
*/
class materialDAO{


    public function addmaterial($form) {
        $connMgr = new ConnectionManager();
        $pdo = $connMgr->getConnection();


        $sql = "insert into learningmaterial (MaterialTitle, MaterialDescription, MaterialType, MaterialURL, LessonID) 
        values (:MaterialTitle, :MaterialDescription, :MaterialType, :MaterialURL, :LessonID);";
        $isAddOK = FALSE;
        try { 

            $stmt = $pdo->prepare($sql);

            $MaterialTitle= $form["MaterialTitle"];
            $MaterialDescription = $form["MaterialDescription"];
            $MaterialType = $form["MaterialType"];
            $MaterialURL = $form["MaterialURL"];
            $LessonID = $form["LessonID"];

            $stmt->bindParam(":MaterialTitle", $MaterialTitle,PDO::PARAM_STR);
            $stmt->bindParam(":MaterialDescription", $MaterialTitle,PDO::PARAM_STR);
            $stmt->bindParam(":MaterialType", $MaterialType,PDO::PARAM_STR);
            $stmt->bindParam(":MaterialURL", $MaterialTitle,PDO::PARAM_STR);
            $stmt->bindParam(":LessonID", $LessonID,PDO::PARAM_STR);

            if ($stmt->execute()) {
                $isAddOK = TRUE;
            }

            $stmt->closeCursor();
            $pdo = null;
        } catch (Exception $e) {
            return $isAddOK;    
        }
    
        return $isAddOK;
    }

    // Retrieve User details
    public function retrieveMaterial($LessonID){
        $conn = new ConnectionManager();
        $pdo = $conn->getConnection();
        
        $sql = 'SELECT MaterialTitle, MaterialDescription, MaterialURL  
                FROM material WHERE LessonID = :LessonID;';
        $stmt = $pdo->prepare($sql);

        $stmt->setFetchMode(PDO::FETCH_ASSOC);
        $stmt->bindParam(':LessonID', $LessonID, PDO::PARAM_STR);
        $stmt->execute();

        $result = null;
        while($row = $stmt->fetch()) {
            $result = new material ($row["MaterialTitle"], $row["MaterialDescription"], $row["MaterialURL "]);
        }
            
        $stmt->closeCursor();
        $pdo = null;
        return $result;
    }

    
    }

   
}
?>