-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 09, 2021 at 10:24 AM
-- Server version: 8.0.18
-- PHP Version: 7.4.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `spm`
--

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
CREATE TABLE IF NOT EXISTS `class` (
  `ClassID` int(255) NOT NULL,
  `TrainerID` int(255) NOT NULL,
  `CourseID` int(255) NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date NOT NULL,
  `StartTime` varchar(255) NOT NULL,
  `EndTime` varchar(255) NOT NULL,
  `ClassName` varchar(255) NOT NULL,
  `ClassSize` int(255) NOT NULL,
  `ClassDay` varchar(255) NOT NULL,
  PRIMARY KEY (`ClassID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`ClassID`, `TrainerID`, `CourseID`, `StartDate`, `EndDate`, `StartTime`, `EndTime`, `ClassName`, `ClassSize`, `ClassDay`) VALUES
(1, 2, 3, '2021-10-08', '2022-04-29', '8am', '11am', 'Class001', 15, ''),
(2, 3, 2, '2021-10-08', '2022-04-29', '3pm', '6pm', 'Class002', 15, ''),
(3, 1, 4, '2021-10-08', '2022-04-29', '1pm', '4pm', 'Class003', 15, ''),
(4, 4, 1, '2021-10-08', '2022-04-29', '10am', '1pm', 'Class004', 15, '');

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `CourseID` int(255) NOT NULL,
  `CourseName` varchar(255) NOT NULL,
  `CourseValidStartDate` date NOT NULL,
  `CourseValidEndDate` date NOT NULL,
  `CreatedBy` int(255) NOT NULL,
  PRIMARY KEY (`CourseID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`CourseID`, `CourseName`, `CourseValidStartDate`, `CourseValidEndDate`, `CreatedBy`) VALUES
(1, 'Advanced Web Application Development', '2021-10-08', '2032-10-31', 3),
(2, 'E-Commerce Technologies', '2021-10-08', '2032-10-31', 2),
(3, 'Internet Security', '2021-10-08', '2032-10-31', 1),
(4, 'Enterprise Information Systems', '2021-10-08', '2032-10-31', 4);

-- --------------------------------------------------------

--
-- Table structure for table `engineer`
--

DROP TABLE IF EXISTS `engineer`;
CREATE TABLE IF NOT EXISTS `engineer` (
  `EngineerID` int(255) NOT NULL,
  `EmployeeName` varchar(255) NOT NULL,
  `CurrentDesignation` varchar(255) NOT NULL,
  `Department` varchar(255) NOT NULL,
  PRIMARY KEY (`EngineerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `engineer`
--

INSERT INTO `engineer` (`EngineerID`, `EmployeeName`, `CurrentDesignation`, `Department`) VALUES
(1, 'Jason Wong', 'Senior Software Engineer', 'Information Technology'),
(2, 'Afiq', 'Senior Software Engineer', 'Information Technology'),
(3, 'Desmond Koh', 'Business Analyst', 'Information Technology'),
(4, 'Alice Lo', 'Project Manager', 'Information Technology');

-- --------------------------------------------------------

--
-- Table structure for table `enrollment`
--

DROP TABLE IF EXISTS `enrollment`;
CREATE TABLE IF NOT EXISTS `enrollment` (
  `CourseID` int(255) NOT NULL,
  `EngineerID` int(255) NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date NOT NULL,
  `AssignedHR` varchar(255) DEFAULT NULL,
  `CourseCompleteRate` int(255) NOT NULL,
  `CompleteStatus` varchar(255) NOT NULL,
  `FinalQuizScore` int(255) NOT NULL,
  `ClassID` int(11) NOT NULL,
  PRIMARY KEY (`CourseID`,`EngineerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `enrollment`
--

INSERT INTO `enrollment` (`CourseID`, `EngineerID`, `StartDate`, `EndDate`, `AssignedHR`, `CourseCompleteRate`, `CompleteStatus`, `FinalQuizScore`, `ClassID`) VALUES
(1, 3, '2021-10-08', '2022-04-29', NULL, 0, 'Not Complete', 0, 4),
(2, 1, '2021-10-08', '2032-10-31', NULL, 0, 'Not Complete', 0, 2),
(2, 4, '2021-10-08', '2022-04-29', NULL, 0, 'Not Complete', 0, 3),
(3, 2, '2021-10-08', '2022-04-29', NULL, 0, 'Not Complete', 0, 1),
(4, 1, '2021-10-08', '2022-04-29', NULL, 0, 'Not Complete', 0, 4);

-- --------------------------------------------------------

--
-- Table structure for table `hr`
--

DROP TABLE IF EXISTS `hr`;
CREATE TABLE IF NOT EXISTS `hr` (
  `HRID` int(255) NOT NULL,
  `EmployeeName` varchar(255) NOT NULL,
  `CurrentDesignation` varchar(255) NOT NULL,
  `Department` varchar(255) NOT NULL,
  PRIMARY KEY (`HRID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hr`
--

INSERT INTO `hr` (`HRID`, `EmployeeName`, `CurrentDesignation`, `Department`) VALUES
(1, 'Tony Wong', 'Senior HR Admin', 'Human Resource'),
(2, 'Mary Lim', 'Senior HR Admin', 'Human Resource'),
(3, 'Paul Ho', 'Junior HR Admin', 'Human Resource'),
(4, 'Sam Poh', 'Director', 'Human Resource');

-- --------------------------------------------------------

--
-- Table structure for table `learningmaterial`
--

DROP TABLE IF EXISTS `learningmaterial`;
CREATE TABLE IF NOT EXISTS `learningmaterial` (
  `MaterialID` int(255) NOT NULL,
  `MaterialTitle` varchar(255) NOT NULL,
  `MaterialDescription` varchar(255) NOT NULL,
  `LessonId` int(255) NOT NULL,
  `LastUpdated` date NOT NULL,
  `MaterialURL` varchar(255) DEFAULT NULL,
  `MaterialType` varchar(255) DEFAULT NULL,
  `CompleteStatus` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`MaterialID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `learningmaterial`
--

INSERT INTO `learningmaterial` (`MaterialID`, `MaterialTitle`, `MaterialDescription`, `LessonId`, `LastUpdated`, `MaterialURL`, `MaterialType`, `CompleteStatus`) VALUES
(1, 'Course Outline', 'Introduction and Week 0 Content', 1, '2021-10-08', 'https://www.euromoney.com/learning/blockchain-explained/what-is-blockchain', NULL, NULL),
(2, 'Course Outline', 'Introduction and Week 0 Content', 2, '2021-10-08', 'https://www.youtube.com/watch?v=SSo_EIwHSd4', NULL, NULL),
(3, 'Course Outline', 'Introduction and Week 0 Content', 3, '2021-10-08', 'https://www.youtube.com/watch?v=SSo_EIwHSd4', NULL, NULL),
(4, 'Course Outline', 'Introduction and Week 0 Content', 4, '2021-10-08', 'https://www.euromoney.com/learning/blockchain-explained/what-is-blockchain', NULL, NULL),
(5, 'Course Outline', 'Week 1 Content', 5, '2021-10-08', 'https://www.youtube.com/watch?v=SSo_EIwHSd4', NULL, NULL),
(6, 'Course Outline', 'Introduction of Javascript', 6, '2021-10-12', 'https://www.w3schools.com/js/DEFAULT.asp', 'URL', 'Not Complete');

-- --------------------------------------------------------

--
-- Table structure for table `lesson`
--

DROP TABLE IF EXISTS `lesson`;
CREATE TABLE IF NOT EXISTS `lesson` (
  `LessonID` int(255) NOT NULL,
  `TrainerID` int(255) NOT NULL,
  `ClassID` int(255) NOT NULL,
  `PrerequisiteLessonID` int(255) DEFAULT NULL,
  `LessonName` varchar(255) NOT NULL,
  PRIMARY KEY (`LessonID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `lesson`
--

INSERT INTO `lesson` (`LessonID`, `TrainerID`, `ClassID`, `PrerequisiteLessonID`, `LessonName`) VALUES
(1, 2, 1, NULL, 'Lesson001'),
(2, 3, 2, NULL, 'Lesson001'),
(3, 1, 3, NULL, 'Lesson001'),
(4, 4, 4, NULL, 'Lesson001'),
(5, 4, 4, NULL, 'Lesson002');

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
CREATE TABLE IF NOT EXISTS `question` (
  `QuizID` int(11) NOT NULL,
  `QuestionID` int(11) NOT NULL,
  `Options` varchar(255) NOT NULL,
  `Answer` varchar(255) NOT NULL,
  `Question` varchar(255) NOT NULL,
  PRIMARY KEY (`QuizID`,`QuestionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`QuizID`, `QuestionID`, `Options`, `Answer`, `Question`) VALUES
(1, 1, 'math.h,studio.h,home.h,sudo.h', '1', 'In the standard library of C programming language, which of the following header file is designed for basic mathematical operations?\r\n'),
(2, 1, 'Yes,No,I dont know', '2', '“Stderr” is a standard error.'),
(3, 1, 'stdio.h, locale.h, stddef.h, stdlib.h, string.h', '1', 'Which of the following header file can be used to define the NULL macro?'),
(4, 1, 'True,False', '0', 'The size of both stack and heap remains the same during run time.'),
(4, 2, 'stdio.h, locale.h, stddef.h, stdlib.h, string.h', '2', 'Which of the following header file can be used to define the NULL macro?');

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
CREATE TABLE IF NOT EXISTS `quiz` (
  `QuizID` int(255) NOT NULL,
  `LastUpdated` date NOT NULL,
  `GradedQuiz` tinyint(1) NOT NULL,
  `PassingGrade` int(255) NOT NULL,
  `LessonID` int(255) NOT NULL,
  `QuizScore` int(255) DEFAULT NULL,
  `QuizName` varchar(255) NOT NULL,
  `QuizTime` int(255) NOT NULL,
  PRIMARY KEY (`QuizID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `quiz`
--

INSERT INTO `quiz` (`QuizID`, `LastUpdated`, `GradedQuiz`, `PassingGrade`, `LessonID`, `QuizScore`, `QuizName`, `QuizTime`) VALUES
(1, '2021-10-08', 0, 50, 1, NULL, 'Quiz001', 20),
(2, '2021-10-08', 0, 50, 2, NULL, 'Quiz001', 20),
(3, '2021-10-08', 0, 50, 3, NULL, 'Quiz001', 20),
(4, '2021-10-08', 0, 50, 4, NULL, 'Quiz001', 20),
(5, '2021-10-08', 0, 50, 5, NULL, 'Quiz002', 20),
(7, '2021-10-12', 0, 50, 7, 100, 'Quiz007', 60);

-- --------------------------------------------------------

--
-- Table structure for table `quizscore`
--

DROP TABLE IF EXISTS `quizscore`;
CREATE TABLE IF NOT EXISTS `quizscore` (
  `EngineerID` int(255) NOT NULL,
  `QuizScore` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `LessonID` int(255) NOT NULL,
  `QuizScoreID` int(255) NOT NULL AUTO_INCREMENT,
  `QuizID` int(255) NOT NULL,
  PRIMARY KEY (`QuizScoreID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `quizscore`
--

INSERT INTO `quizscore` (`EngineerID`, `QuizScore`, `LessonID`, `QuizScoreID`, `QuizID`) VALUES
(1, '75', 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `trainer`
--

DROP TABLE IF EXISTS `trainer`;
CREATE TABLE IF NOT EXISTS `trainer` (
  `TrainerID` int(255) NOT NULL,
  `EmployeeName` varchar(255) NOT NULL,
  `CurrentDesignation` varchar(255) NOT NULL,
  `Department` varchar(255) NOT NULL,
  PRIMARY KEY (`TrainerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `trainer`
--

INSERT INTO `trainer` (`TrainerID`, `EmployeeName`, `CurrentDesignation`, `Department`) VALUES
(1, 'Nova Choi', 'Senior Admin', 'Staff Development'),
(2, 'Ivy Teo', 'Senior Admin', 'Staff Development'),
(3, 'Jeremy Tan', 'Director', 'Staff Development'),
(4, 'Rachel Goh', 'Assistance Admin', 'Staff Development');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
