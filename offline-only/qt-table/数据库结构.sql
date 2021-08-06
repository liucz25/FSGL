/*
 Navicat Premium Data Transfer

 Source Server         : fsgl-jj
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 13/06/2021 20:29:05
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for group
-- ----------------------------
DROP TABLE IF EXISTS "group";
CREATE TABLE "group" (
  "groupId" INTEGER NOT NULL,
  "name" TEXT,
  "TEXT",
  PRIMARY KEY ("groupId")
);

-- ----------------------------
-- Table structure for person
-- ----------------------------
DROP TABLE IF EXISTS "person";
CREATE TABLE "person" (
  "personId" INTEGER(32) NOT NULL,
  "name" TEXT(128),
  "zhichengId" integer,
  "groupId" INTEGER,
  "zhiwuId" INTEGER,
  "zhizescore" real,
  "workscore" real,
  "TEXT",
  PRIMARY KEY ("personId"),
  CONSTRAINT "pg" FOREIGN KEY ("groupId") REFERENCES "group" ("groupId") ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT "pzc" FOREIGN KEY ("zhichengId") REFERENCES "zhicheng" ("zhichengID") ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT "pzw" FOREIGN KEY ("zhiwuId") REFERENCES "zhiwu" ("zhiwuId") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for pmoney
-- ----------------------------
DROP TABLE IF EXISTS "pmoney";
CREATE TABLE "pmoney" (
  "moneyId" INTEGER NOT NULL,
  "personId" INTEGER,
  "month" TEXT,
  "zhiwuScore" real,
  "workScore" real,
  "zhiwumoney" real,
  "workmoney" real,
  "worktypemoney" real,
  "allmoney" real,
  PRIMARY KEY ("moneyId"),
  CONSTRAINT "mp" FOREIGN KEY ("personId") REFERENCES "person" ("personId") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for pworkload
-- ----------------------------
DROP TABLE IF EXISTS "pworkload";
CREATE TABLE "pworkload" (
  "pworkId" INTEGER NOT NULL,
  "personId" INTEGER,
  "workId" INTEGER,
  "month" TEXT,
  "number" INTEGER,
  "score" real,
  "money" real,
  "bili" real,
  PRIMARY KEY ("pworkId"),
  CONSTRAINT "wlp" FOREIGN KEY ("personId") REFERENCES "person" ("personId") ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT "wlw" FOREIGN KEY ("workId") REFERENCES "worktype" ("worktypeId") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for pworktype
-- ----------------------------
DROP TABLE IF EXISTS "pworktype";
CREATE TABLE "pworktype" (
  "pWorkTypeId" INTEGER NOT NULL,
  "personId" INTEGER,
  "worktypeId" INTEGER,
  "month" text,
  "atwork" integer,
  "number" INTEGER,
  "bili" real,
  "money" real,
  PRIMARY KEY ("pWorkTypeId"),
  CONSTRAINT "wtp" FOREIGN KEY ("personId") REFERENCES "person" ("personId") ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT "ww" FOREIGN KEY ("worktypeId") REFERENCES "worktype" ("worktypeId") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for pworktypemoney
-- ----------------------------
DROP TABLE IF EXISTS "pworktypemoney";
CREATE TABLE "pworktypemoney" (
  "pworktypeId" INTEGER NOT NULL,
  "personId" INTEGER,
  "month" TEXT,
  "worktypyId" INTEGER,
  "worktypemoney" real,
  PRIMARY KEY ("pworktypeId"),
  CONSTRAINT "pwlmp" FOREIGN KEY ("personId") REFERENCES "person" ("personId") ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT "pwlmw" FOREIGN KEY ("worktypyId") REFERENCES "worktype" ("worktypeId") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for workload
-- ----------------------------
DROP TABLE IF EXISTS "workload";
CREATE TABLE "workload" (
  "workId" INTEGER NOT NULL,
  "name" TEXT,
  "score" real,
  "TEXT",
  PRIMARY KEY ("workId")
);

-- ----------------------------
-- Table structure for worktype
-- ----------------------------
DROP TABLE IF EXISTS "worktype";
CREATE TABLE "worktype" (
  "worktypeId" INTEGER NOT NULL,
  "workname" TEXT,
  "dangemoney" TEXT,
  PRIMARY KEY ("worktypeId")
);

-- ----------------------------
-- Table structure for zhicheng
-- ----------------------------
DROP TABLE IF EXISTS "zhicheng";
CREATE TABLE "zhicheng" (
  "zhichengID" INTEGER(64) NOT NULL,
  "name" TEXT,
  "score" real,
  "groupId" INTEGER,
  "TEXT",
  PRIMARY KEY ("zhichengID"),
  CONSTRAINT "zg" FOREIGN KEY ("groupId") REFERENCES "group" ("groupId") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for zhiwu
-- ----------------------------
DROP TABLE IF EXISTS "zhiwu";
CREATE TABLE "zhiwu" (
  "zhiwuId" INTEGER(64) NOT NULL,
  "name" TEXT,
  "score" real,
  PRIMARY KEY ("zhiwuId")
);

PRAGMA foreign_keys = true;
