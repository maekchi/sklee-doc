import re

white_space = re.compile(r"\s+")


class ReqDocument:
    def __init__(self):
        self.title = None
        self.user_id = None
        self.user_dept = None
        self.user_name = None
        self.request_date = None
        self.doc_num = None

    def __str__(self):
        return f"""        문서제목 : {self.title}
        문서번호 : {self.doc_num}
        기안부서 : {self.user_dept}
        기안자 ID : {self.user_id}
        기안자 : {self.user_name}
        기안일 : {self.request_date}"""


class ReqDocumentIp(ReqDocument):
    def __init__(self):
        super().__init__()
        self.wire_mac = None
        self.wireless_mac = None

    def __str__(self):
        parent = super(ReqDocumentIp, self).__str__()
        return f"""{parent}
        유선MAC : {self.wire_mac}
        무선MAC : {self.wireless_mac}"""


class Parser:
    def __init__(self):
        self.parse_func = self.parse_unknown
        self.doc = None

    def __str__(self):
        return str(self.doc)

    def parse_unknown(self, line: str, line_title: str, line_cnt: int) -> (bool):
        pass

    def parse_ip(self, line: str, line_title: str, line_cnt: int) -> (bool):
        if line_cnt == 5:
            if line_title.startswith(self.doc.title):
                self.doc.doc_num = "기안-" + line_title.split("-", 1)[1]
        elif line_cnt == 6:
            if line_title != "기안일":
                return (True)
        elif line_cnt == 7:
            self.doc.request_date = line.strip()

        elif line_cnt == 8:
            if line_title != "기안자":
                return (True)
        elif line_cnt == 9:
            self.doc.user_name = line_title
        elif line_cnt == 10:
            if line_title != "기안부서":
                return (True)
        elif line_cnt == 11:
            self.doc.user_dept = line_title
        elif line_cnt == 12:
            if line_title != "이메일":
                return (True)
        elif line_cnt == 13:
            self.doc.user_id = line_title.split("@", 1)[0]
        elif line_cnt == 14:
            if line_title != "유선MAC주소":
                return (True)
        elif line_cnt == 15:
            self.doc.wire_mac = line_title
        elif line_cnt == 16:
            if line_title != "무선MAC주소":
                return (True)
        elif line_cnt == 17:
            self.doc.wireless_mac = line_title

        return (False)

    def parse(self, text: str):
        try:
            line_cnt = 1
            text_line = 0
            for line in text.split("\n"):
                line_title = white_space.sub("", line)
                text_line += 1
                if not line_title:
                    continue

                if line_cnt == 1:
                    if line_title != "결재문서":
                        raise ParserException(str("문서 처음은 반드시 결재문서 로 시작하는 문서 복사본이어야됩니다."))
                elif line_cnt == 3:
                    if line_title == "IP신청서":
                        self.doc = ReqDocumentIp()
                        self.doc.title = "IP신청서"
                        self.parse_func = self.parse_ip
                else:
                    cont = self.parse_func(line=line, line_title=line_title, line_cnt=line_cnt)
                    if cont:
                        continue
                line_cnt += 1

        except Exception as ex:
            raise ParserException(str(ex))


class ParserException(Exception):
    pass
