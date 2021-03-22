totalMoney = 0 '�����Ѷ�
    index = -1 '��ʼ��checkbox�ؼ�ID��ţ�
    flag = 0 '�����ļ��Ƿ�Ķ��ı�־
    set fso = createobject("scripting.filesystemobject")
    '///////////////////�ļ�����ʱ����ȡ�����ļ�������������С��λ��////////
    Sub Window_onLoad
    if not(fso.fileexists("consume.ini")) then '�����������ļ��򴴽���
    fso.createtextfile("consume.ini").close
    end
    if
    window.resizeTo 638, 495 '����������С��λ�ã�
    window.moveTo 200, 100
    addRow 0, "hoho", "2007-1-1", "���ڶ�"
    '������һ���С��Լ����㲻���ף�������������bug��
    document.all.namedItem("mytable").rows(1).style.display = "none"
    '�������в��ɼ�;
    addRow 0, "hoho", "2007-1-1", "���ڶ�"
    '������һ���С��Լ����㲻���ף�������������bug��
    document.all.namedItem("mytable").rows(2).style.display = "none"
    '�������в��ɼ�;
    readFile("consume.ini")
    End Sub
        '//////////////////��ȡ�ļ�//////////////////
    Function readFile(filename)
    set file = fso.opentextfile(filename, 1, 1)
    do
        while file.atendofline < > true '���ļ�һֱ���ļ�β��
    str = split(file.readline, "#")
    '��#��־�ָ�û��(�ܹ����ĸ����ֱ�־)
    addRow str(1), str(2), str(3), str(4)
    '���������Ԫ�����ݷֱ�Ϊ....
    loop
    End Function
        '////////////////���ӱ��У���Ԫ��///////////
    Function addRow(cnum, ctype, cdate, cday)
    index = index + 1 '����Լ�1
    set objTable = document.all.namedItem("mytable")
    '����ID��ȡ�������
    set newrow = objTable.insertRow()
    '����һ��
    newrow.className = "row_add"
    '���ø��е���ʽ��
    newrow.onmouseover = getRef("change_bgcolor")
    newrow.onmouseout = getRef("back_bgcolor")
    newrow.onclick = getRef("chooseOBJ")
    var = "#" & cnum & "#" & ctype & "#" & cdate & "#" & cday
    str = split(var, "#")
    str(0) = "<input type=checkbox id='delcheck'&index>"
    for i = 0 to 4
    set newcell = newrow.insertCell()
    '���뵥Ԫ�񣬲����õ�Ԫ���ֵ��
    newcell.innerhtml = str(i)
    next
    totalMoney = totalMoney + clng(cnum)
    '���������Ѷ��ֵ����������ʾ��
    consume.innerHTML = "�����ܶ" & totalMoney & "Ԫ"
    End Function
        '///////////////�ı���󱳾�//////////////
    Function change_bgcolor()
    me.className = "new_row_add"
    End Function
        '/////////////����ԭ������ɫ//////////////
    Function back_bgcolor()
    me.className = "row_add"
    End Function
        '////////////ѡ������/////////
    Function chooseOBJ()
    if me.cells(0).children(0).checked = true then
    me.cells(0).children(0).checked = false
    else
        me.cells(0).children(0).checked = true
    end
    if
    End Function
        '/////////////////"ɾ��"һ����Ԫ��///////////////
    Function delRow()
    for i = 0 to index
    if delcheck(i).checked = true then
    set tag = delcheck(i).parentelement.parentelement '���ø�checkbox���ڵ��У�
    tag.style.display = "none"
    '��ʵ����ν��ɾ�����ǰ�������Ϊ����ʾ��
    totalMoney = totalMoney - clng(tag.cells(1).innertext)
    consume.innerHTML = "�����ܶ" & totalMoney & "Ԫ"
    tag.cells(1).innertext = "0"
    '���Ѷ�����Ϊ0��
    end
    if
    next
    flag = 1 '���ִ����ɾ�����������־�ļ��Ѿ��Ķ���
    End Function
        '////////////////////������������Ƿ���ȷ////////////
    Function check(value)
    if not(isnumeric(value)) then
    msgbox "�������ѽ��������������!", 64, "�ر���ʾ"
    elseif value < 1 then
    msgbox "���Ǯ�ѵ�Խ��Խ��?", 64, "�ر���ʾ"
    else
        flag = 1
    addRow money.value, cstype.options(cstype.selectedIndex).innerText, date, weekdayname(weekday(date))
    csmonth.selectedIndex = month(date())
    '�·�checkboxת����ǰ�·ݣ�
    selectChange(monthname(month(date())))
    '������ʾΪ��ǰ�·ݵ����ݣ�
    end
    if
    money.select()
    'money�����ѡ����
    End Function
        '////////////////////////����·�checkbox�仯//////////////
    Function selectChange(choose)
    '78�У�
    totalMoney = 0
    for i = 0 to index
    set tag = delcheck(i).parentelement.parentelement
    mName = monthname(month(tag.cells(3).innertext))
    '��ȡ���ݵ��·ݣ�
    if trim(choose) = "һ��"
    and tag.cells(1).innertext < > "0"
    then
    tag.style.display = ""
    totalMoney = totalMoney + clng(tag.cells(1).innertext)
    elseif mName < > trim(choose) or tag.cells(1).innertext = "0"
    then
    tag.style.display = "none"
    else
        tag.style.display = ""
    totalMoney = totalMoney + clng(tag.cells(1).innertext)
    end
    if
    next
    consume.innerHTML = "�����ܶ" & totalMoney & "Ԫ"
    End Function
        '////////////ȫѡ��ȫ��ѡ��ť���ƴ���//////
    Function selectAll()
    '96�У�
    if mybutton.value = "ȫ��ѡ��"
    then
    for i = 0 to index
    delcheck(i).checked = true
    next
    mybutton.value = "ȫ��ѡ��"
    else
        for i = 0 to index
    delcheck(i).checked = false
    next
    mybutton.value = "ȫ��ѡ��"
    end
    if
    End Function
        '/////////////�������˳�ʱ//////////////////
    Sub Window_onunLoad()
    if flag = 1 then '�ļ�����Ѿ���־�˸Ķ�������ʾ�Ƿ񱣴棻
    msg = msgbox("��ʾ����������Ѿ����ģ��Ƿ񱣴�?", vbyesno + vbExclamation, "��������")
    if msg = 6 then '���ѡ���ˡ��ǡ���
    selectChange("һ��")
    '��ǰ������ʾ������Ϊȫ������ݣ�
    for i = 0 to index
    set tag = delcheck(i).parentelement.parentelement
    if tag.cells(1).innertext < > "0"
    then
    txt = txt & "#" & tag.cells(1).innertext & "#" & tag.cells(2).innertext & "#"
    txt = txt & tag.cells(3).innertext & "#" & tag.cells(4).innertext & vbcrlf
    end
    if
    next
    set file = fso.opentextfile("consume.ini", 2, 1)
    '����д���ļ���
    file.write(txt).close
    end
    if
    end
    if
    End Sub