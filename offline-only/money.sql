/*
 Navicat Premium Data Transfer

 Source Server         : rygl
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 21/09/2020 19:58:43
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for money
-- ----------------------------
DROP TABLE IF EXISTS "money";
CREATE TABLE "money" (
  "mid" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "pid" INTEGER,
  "month" TEXT,
  "mrinumber" INTEGER,
  "mrimoney" real,
  "nightnumber" INTEGER,
  "nightmoney" real,
  "healthmoney" real,
  "yiliantinumber" INTEGER,
  "yiliantimoney" real,
  "zhiwujintie" real,
  "jianzhi" real,
  "canhui" real,
  "rankscore" real,
  "rankmoney" real,
  "workscore" real,
  "workmoney" real,
  "allmoney" real
);

-- ----------------------------
-- Auto increment value for money
-- ----------------------------

PRAGMA foreign_keys = true;
