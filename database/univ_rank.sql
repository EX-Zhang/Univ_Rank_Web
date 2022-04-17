/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80028
Source Host           : localhost:3306
Source Database       : univrank

Target Server Type    : MYSQL
Target Server Version : 80028
File Encoding         : 65001

Date: 2022-04-16 18:05:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for univ_rank
-- ----------------------------
DROP TABLE IF EXISTS `univ_rank`;
CREATE TABLE `univ_rank` (
  `Univ_ID` int NOT NULL,
  `Univ_Rank` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Univ_Name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Univ_Reign` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Univ_Score` varchar(255) DEFAULT NULL,
  `Univ_Stud_Rate` varchar(255) DEFAULT NULL,
  `Univ_Prof_Rate` varchar(255) DEFAULT NULL,
  `Univ_Prof_Stud_Rate` varchar(255) DEFAULT NULL,
  `Univ_Ref_Rate` varchar(255) DEFAULT NULL,
  `Univ_Acad_Repu` varchar(255) DEFAULT NULL,
  `Univ_Employer_Repu` varchar(255) DEFAULT NULL,
  `Univ_Reign_EN` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Univ_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
