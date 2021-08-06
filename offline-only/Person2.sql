/*
 Navicat Premium Data Transfer

 Source Server         : rygl
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 21/09/2020 19:57:37
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for Person
-- ----------------------------
DROP TABLE IF EXISTS "Person";
CREATE TABLE "Person" (
  "personID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" TEXT,
  "roletype" TEXT,
  "canyufenpei" integer,
  "junfen" integer,
  "workloadfenpei" integer,
  "rankscore" real,
  "atwork" integer,
  "atnight" integer,
  "athealth" integer,
  "atmri" integer,
  "atyilianti" integer,
  "zhiwujintie" integer,
  "jianzhi" integer,
  "canhui" integer
);

-- ----------------------------
-- Records of Person
-- ----------------------------
INSERT INTO "Person" VALUES (4, 'hjby', '医师', 1, 1, 1, NULL, 1, 1, 1, 1, 1, 111, 222, 33);
INSERT INTO "Person" VALUES (6, '张三', '医师', 1, 1, NULL, NULL, 1, NULL, NULL, 1, NULL, '', '', '');
INSERT INTO "Person" VALUES (10, '', '医师', 1, 1, NULL, NULL, NULL, NULL, 1, NULL, NULL, '', '', '');
INSERT INTO "Person" VALUES (12, '李四', '医师', 1, NULL, NULL, NULL, 1, NULL, NULL, 1, NULL, '掐', '钱', '钱钱12');
INSERT INTO "Person" VALUES (13, 133, '医师', 1, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, 1333, 13, 13);
INSERT INTO "Person" VALUES (14, '', '医师', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '');
INSERT INTO "Person" VALUES (17, '', '医师', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '发大V', '', '');
INSERT INTO "Person" VALUES (18, '', '医师', NULL, 1, 1, NULL, NULL, NULL, NULL, 1, 1, '', '', '');
INSERT INTO "Person" VALUES (19, '', '医师', NULL, 1, NULL, NULL, NULL, NULL, 1, 1, 1, '', '', '');
INSERT INTO "Person" VALUES (20, '', '医师', NULL, NULL, NULL, NULL, NULL, NULL, 1, 1, NULL, '', '', '');

-- ----------------------------
-- Auto increment value for Person
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 22 WHERE name = 'Person';

PRAGMA foreign_keys = true;
