-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 21, 2021 at 03:36 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
-- Table structure for table `attempt`
--

CREATE TABLE `attempt` (
  `QuizID` int(255) NOT NULL,
  `QuestionID` int(255) NOT NULL,
  `EngineerID` int(255) NOT NULL,
  `CompleteStatus` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `ClassID` int(255) NOT NULL,
  `TrainerID` int(255) NOT NULL,
  `CourseID` int(255) NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date NOT NULL,
  `StartTime` varchar(255) NOT NULL,
  `EndTime` varchar(255) NOT NULL,
  `ClassName` varchar(255) NOT NULL,
  `ClassSize` int(255) NOT NULL,
  `ClassDay` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`ClassID`, `TrainerID`, `CourseID`, `StartDate`, `EndDate`, `StartTime`, `EndTime`, `ClassName`, `ClassSize`, `ClassDay`) VALUES
(1, 2, 3, '2021-10-08', '2022-04-29', '8am', '11am', 'Class001', 15, 'Wed'),
(2, 3, 2, '2021-10-08', '2022-04-29', '3pm', '6pm', 'Class002', 15, 'Thurs'),
(3, 1, 4, '2021-10-08', '2022-04-29', '1pm', '4pm', 'Class003', 15, 'Mon'),
(4, 4, 1, '2021-10-08', '2022-04-29', '10am', '1pm', 'Class004', 15, 'Fri');

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `CourseID` int(255) NOT NULL,
  `CourseName` varchar(255) NOT NULL,
  `CourseValidStartDate` date NOT NULL,
  `CourseValidEndDate` date NOT NULL,
  `CreatedBy` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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

CREATE TABLE `engineer` (
  `EngineerID` int(255) NOT NULL,
  `EmployeeName` varchar(255) NOT NULL,
  `CurrentDesignation` varchar(255) NOT NULL,
  `Department` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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

CREATE TABLE `enrollment` (
  `CourseID` int(255) NOT NULL,
  `ClassID`  int(255) NOT NULL,
  `EngineerID` int(255) NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date NOT NULL,
  `AssignedHR` varchar(255) DEFAULT NULL,
  `CourseCompleteRate` int(255) NOT NULL,
  `CompleteStatus` varchar(255) NOT NULL,
  `FinalQuizScore` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `enrollment`
--

INSERT INTO `enrollment` (`CourseID`, `ClassID`, `EngineerID`, `StartDate`, `EndDate`, `AssignedHR`, `CourseCompleteRate`, `CompleteStatus`, `FinalQuizScore`) VALUES
(1, 4, 3, '2021-10-08', '2022-04-29', NULL, 0, 'Not Complete', 0),
(2, 2, 4, '2021-10-08', '2022-04-29', NULL, 0, 'Not Complete', 0),
(3, 1, 2, '2021-10-08', '2022-04-29', NULL, 0, 'Not Complete', 0),
(4, 3, 1, '2021-10-08', '2022-04-29', NULL, 0, 'Not Complete', 0);

-- --------------------------------------------------------

--
-- Table structure for table `hr`
--

CREATE TABLE `hr` (
  `HRID` int(255) NOT NULL,
  `EmployeeName` varchar(255) NOT NULL,
  `CurrentDesignation` varchar(255) NOT NULL,
  `Department` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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

CREATE TABLE `learningmaterial` (
  `MaterialID` int(255) NOT NULL,
  `MaterialTitle` varchar(255) NOT NULL,
  `MaterialDescription` varchar(255) NOT NULL,
  `LessonId` int(255) NOT NULL,
  `LastUpdated` date NOT NULL,
  `MaterialURL` varchar(255) DEFAULT NULL,
  `MaterialType` varchar(255) DEFAULT NULL,
  `CompleteStatus` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `learningmaterial`
--

INSERT INTO `learningmaterial` (`MaterialID`, `MaterialTitle`, `MaterialDescription`, `LessonId`, `LastUpdated`, `MaterialURL`, `MaterialType`, `CompleteStatus`) VALUES
(1, 'Course Outline', 'Introduction and Week 0 Content', 1, '2021-10-08', NULL, NULL, NULL),
(2, 'Course Outline', 'Introduction and Week 0 Content', 2, '2021-10-08', NULL, NULL, NULL),
(3, 'Course Outline', 'Introduction and Week 0 Content', 3, '2021-10-08', NULL, NULL, NULL),
(4, 'Course Outline', 'Introduction and Week 0 Content', 4, '2021-10-08', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `lesson`
--

CREATE TABLE `lesson` (
  `LessonID` int(255) NOT NULL,
  `TrainerID` int(255) NOT NULL,
  `ClassID` int(255) NOT NULL,
  `PrerequisiteLessonID` int(255) DEFAULT NULL,
  `LessonName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lesson`
--

INSERT INTO `lesson` (`LessonID`, `TrainerID`, `ClassID`, `PrerequisiteLessonID`, `LessonName`) VALUES
(1, 2, 1, NULL, 'Lesson001'),
(2, 3, 2, NULL, 'Lesson001'),
(3, 1, 3, NULL, 'Lesson001'),
(4, 4, 4, NULL, 'Lesson001');

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
  `QuizID` int(11) NOT NULL,
  `QuestionID` int(11) NOT NULL,
  `Options` varchar(255) NOT NULL,
  `Answer` varchar(255) NOT NULL,
  `Question` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`QuizID`, `QuestionID`, `Options`, `Answer`, `Question`) VALUES
(1, 1, 'math.h,studio.h,home.h,sudo.h', 'sudo.h', 'In the standard library of C programming language, which of the following header file is designed for basic mathematical operations?\r\n'),
(2, 1, 'True,False', 'False', '“Stderr” is a standard error.'),
(3, 1, 'stdio.h, locale.h, stddef.h, stdlib.h, string.h', 'string.h', 'Which of the following header file can be used to define the NULL macro?'),
(4, 1, 'True,False', 'True', 'The size of both stack and heap remains the same during run time.');

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

CREATE TABLE `quiz` (
  `QuizID` int(255) NOT NULL,
  `LastUpdated` date NOT NULL,
  `GradedQuiz` tinyint(1) NOT NULL,
  `PassingGrade` int(255) NOT NULL,
  `LessonID` int(255) NOT NULL,
  `QuizScore` int(255) DEFAULT NULL,
  `QuizName` varchar(255) NOT NULL,
  `QuizTime` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `quiz`
--

INSERT INTO `quiz` (`QuizID`, `LastUpdated`, `GradedQuiz`, `PassingGrade`, `LessonID`, `QuizScore`, `QuizName`,`QuizTime`) VALUES
(1, '2021-10-08', 0, 50, 1, NULL, 'Quiz001', 60),
(2, '2021-10-08', 0, 50, 2, NULL, 'Quiz001', 60),
(3, '2021-10-08', 0, 50, 3, NULL, 'Quiz001', 60),
(4, '2021-10-08', 0, 50, 4, NULL, 'Quiz001', 60);

-- --------------------------------------------------------

--
-- Table structure for table `trainer`
--

CREATE TABLE `trainer` (
  `TrainerID` int(255) NOT NULL,
  `EmployeeName` varchar(255) NOT NULL,
  `CurrentDesignation` varchar(255) NOT NULL,
  `Department` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `trainer`
--

INSERT INTO `trainer` (`TrainerID`, `EmployeeName`, `CurrentDesignation`, `Department`) VALUES
(1, 'Nova Choi', 'Senior Admin', 'Staff Development'),
(2, 'Ivy Teo', 'Senior Admin', 'Staff Development'),
(3, 'Jeremy Tan', 'Director', 'Staff Development'),
(4, 'Rachel Goh', 'Assistance Admin', 'Staff Development');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attempt`
--
ALTER TABLE `attempt`
  ADD PRIMARY KEY (`QuizID`,`QuestionID`);

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`ClassID`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`CourseID`);

--
-- Indexes for table `engineer`
--
ALTER TABLE `engineer`
  ADD PRIMARY KEY (`EngineerID`);

--
-- Indexes for table `enrollment`
--
ALTER TABLE `enrollment`
  ADD PRIMARY KEY (`CourseID`,`EngineerID`);

--
-- Indexes for table `hr`
--
ALTER TABLE `hr`
  ADD PRIMARY KEY (`HRID`);

--
-- Indexes for table `learningmaterial`
--
ALTER TABLE `learningmaterial`
  ADD PRIMARY KEY (`MaterialID`);

--
-- Indexes for table `lesson`
--
ALTER TABLE `lesson`
  ADD PRIMARY KEY (`LessonID`);

--
-- Indexes for table `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`QuizID`,`QuestionID`);

--
-- Indexes for table `quiz`
--
ALTER TABLE `quiz`
  ADD PRIMARY KEY (`QuizID`);

--
-- Indexes for table `trainer`
--
ALTER TABLE `trainer`
  ADD PRIMARY KEY (`TrainerID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;