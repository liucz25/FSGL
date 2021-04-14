#include"dcmtk/config/osconfig.h"

#include"dcmtk/dcmdata/dctk.h"

#include<iostream>



using namespace std;

int main()

{

    DcmFileFormat fileformat;

    
    OFCondition oc = fileformat.loadFile("D:/code/fsgl/offline-only/dcmtk/dcmtk-src/test1/dcmtk-test-1/x64/Debug/111.dcm");

    if (oc.good()) {

        OFString patientName;

        if (fileformat.getDataset()->findAndGetOFString(DCM_PatientName, patientName).good())

        {

            cout << "Patient Name:" << patientName.data() << endl;

        }

    }



    system("pause");



    return 0;

}