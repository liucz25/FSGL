/*
 Navicat Premium Data Transfer

 Source Server         : rygl
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 21/09/2020 19:56:41
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
-- Auto increment value for Person
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 22 WHERE name = 'Person';

PRAGMA foreign_keys = true;
