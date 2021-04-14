//ÊµÀý³ÌÐò

//#include "stdafx.h"
#include <iostream>
#include "D:\code\fsgl\offline-only\dcmtk\dcmtk-lib\include\dcmtk\config\osconfig.h"
#include "D:\code\fsgl\offline-only\dcmtk\dcmtk-lib\include\dcmtk\dcmdata\dctk.h"

bool ReadPatientName(DcmFileFormat& fileformat, std::string& filePath) {
	OFCondition status = fileformat.loadFile(filePath.c_str());
	if (!status.good()) {
		std::cout << "Load diconm file error:" << status.text() << std::endl;
		return false;
	}
	OFString PatientName;

}