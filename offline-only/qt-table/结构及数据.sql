/*
 Navicat Premium Data Transfer

 Source Server         : fsgl-jj
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 13/06/2021 20:30:38
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
-- Records of group
-- ----------------------------
INSERT INTO "group" VALUES (1, '医师', NULL);
INSERT INTO "group" VALUES (2, '护士', NULL);
INSERT INTO "group" VALUES (3, '技师', NULL);
INSERT INTO "group" VALUES (4, '汇总', NULL);

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
-- Records of person
-- ----------------------------
INSERT INTO "person" VALUES (1, '白秋立', NULL, 1, NULL, NULL, NULL, NULL);
INSERT INTO "person" VALUES (2, '赵会军', NULL, 1, NULL, NULL, NULL, NULL);
INSERT INTO "person" VALUES (3, '诊断汇总', NULL, 4, NULL, NULL, NULL, NULL);
INSERT INTO "person" VALUES (4, '护士汇总', NULL, 4, NULL, NULL, NULL, NULL);
INSERT INTO "person" VALUES (5, '技术汇总', NULL, 4, NULL, NULL, NULL, NULL);
INSERT INTO "person" VALUES (6, '贾雪霞', NULL, 2, NULL, NULL, NULL, NULL);
INSERT INTO "person" VALUES (7, '宋志丽', NULL, 3, NULL, NULL, NULL, NULL);

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
-- Records of pmoney
-- ----------------------------
INSERT INTO "pmoney" VALUES (1, 1, 202101, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "pmoney" VALUES (2, 1, 202102, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "pmoney" VALUES (3, 2, 202101, NULL, NULL, NULL, NULL, NULL, NULL);

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
-- Records of pworkload
-- ----------------------------
INSERT INTO "pworkload" VALUES (1, 1, 1, 202101, 33, NULL, NULL, NULL);
INSERT INTO "pworkload" VALUES (2, 1, 2, 202101, 44, NULL, NULL, NULL);
INSERT INTO "pworkload" VALUES (3, 2, 1, 202101, 55, NULL, NULL, NULL);

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
-- Records of pworktype
-- ----------------------------
INSERT INTO "pworktype" VALUES (1, 1, 1, 202101, 1, 21, NULL, NULL);
INSERT INTO "pworktype" VALUES (2, 1, 2, 202101, 1, 23, NULL, NULL);
INSERT INTO "pworktype" VALUES (3, 2, 1, 202101, 1, 34, NULL, NULL);

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
-- Records of pworktypemoney
-- ----------------------------
INSERT INTO "pworktypemoney" VALUES (1, 1, 202101, 1, NULL);
INSERT INTO "pworktypemoney" VALUES (2, 1, 202101, 2, NULL);
INSERT INTO "pworktypemoney" VALUES (3, 2, 202101, 1, NULL);

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
-- Records of workload
-- ----------------------------
INSERT INTO "workload" VALUES (1, '写平片', 1.0, NULL);
INSERT INTO "workload" VALUES (2, '写CT', 1.0, NULL);
INSERT INTO "workload" VALUES (3, '写MRI', 1.0, NULL);
INSERT INTO "workload" VALUES (4, '写CT增强', 1.0, NULL);
INSERT INTO "workload" VALUES (5, '写核磁增强', 1.0, NULL);
INSERT INTO "workload" VALUES (6, '写造影', 1.0, NULL);
INSERT INTO "workload" VALUES (7, '审平片', 1.0, NULL);
INSERT INTO "workload" VALUES (8, '审CT', 1.0, NULL);

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
-- Records of worktype
-- ----------------------------
INSERT INTO "worktype" VALUES (1, '夜班', 60);
INSERT INTO "worktype" VALUES (2, '体检', NULL);
INSERT INTO "worktype" VALUES (3, '社区', NULL);
INSERT INTO "worktype" VALUES (4, '医联体', NULL);

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
-- Records of zhicheng
-- ----------------------------
INSERT INTO "zhicheng" VALUES (1, '住院医师', 1.0, 1, NULL);
INSERT INTO "zhicheng" VALUES (2, '执业医师', 1.1, 1, NULL);
INSERT INTO "zhicheng" VALUES (3, '主治医师', 1.2, 1, NULL);
INSERT INTO "zhicheng" VALUES (4, '副主任医师', 1.4, 1, NULL);
INSERT INTO "zhicheng" VALUES (5, '主任医师', 1.6, 1, NULL);
INSERT INTO "zhicheng" VALUES (6, '护士', 1.0, 2, NULL);
INSERT INTO "zhicheng" VALUES (7, '护师', 1.1, 2, NULL);
INSERT INTO "zhicheng" VALUES (8, '主管护师', 1.3, 2, NULL);
INSERT INTO "zhicheng" VALUES (9, '技士', 1.0, 3, NULL);
INSERT INTO "zhicheng" VALUES (10, '技师', 1.0, 3, NULL);
INSERT INTO "zhicheng" VALUES (11, '汇总', NULL, 4, NULL);

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

-- ----------------------------
-- Records of zhiwu
-- ----------------------------
INSERT INTO "zhiwu" VALUES (1, '主任助理', 0.5);
INSERT INTO "zhiwu" VALUES (2, '组长', 0.3);
INSERT INTO "zhiwu" VALUES (3, '护士长', 0.3);

PRAGMA foreign_keys = true;
