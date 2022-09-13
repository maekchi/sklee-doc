from sample.gui import GuiScreen
from sample.parser import Parser
import sys

version = "1.0.0"


test_text = """
결재문서
select
IP 신청서
문 서 번 호

IP 신청서-22-224  
결재  책임  팀장  팀장     본부장
1
  이순신
2
이사람인
3
  사장님
   
4
손권
2022-07-29
이순신
2022-07-29
이사람
2022-08-01
사장님
   
2022-08-01
손권
합의               
             
             
기   안   일

2022-07-29 14:03
기   안   자

이순신
T    e    l

직         급

책임
기 안 부 서

테스트부서
수   신  처

정보보안팀
수신 및 참조

정보보안팀
제         목

IP 변경 신청서 - 이순신
구분

 IP 생성  IP 변경  IP 삭제

이메일

lssin@ez_test.com

단말기

 노트북  데스크탑  기타 ( )

MAC
주소

유선MAC주소

기존 = 30:00:22:aa:11:dd

변경 = 00:ee:44:cc:dd:33

무선MAC주소

기존 = ff:5d:11:cc:02:61

변경 = cc:90:44:55:11:01

네트워크 망

 업무망  Cloud망  연구소망

유ㆍ무선
사용여부

 유선 사용  무선 사용  유ㆍ무선 사용

사용 기간

년  월  일 ~   년  월  일 (임시 사용자만 기재)

요청사유
(상세기술)

기존 장비에서 새  장비로 교체함으로써 mac주소 및 ip 이동 신청드립니다.

[참고사항]
 - 결재선은 요청자 → 요청자 부서 팀장
※ IP 변경 및 삭제 신청 시 요청 내용에 기존 사용하던 IP기입 필수
※ 자산 변경 시 기존 사용 중인 IP와 신규 자산의  MAC 주소 기입 필수



참 조 문 서

선택된 문서가 없습니다.


저장
파일첨부파일 갯수 0개
파일찾기
선택된 파일 없음
최민식2022-07-29 17:46:10
이순신추후 기안 작성시 요청 사유에 상세하게 기입 부탁드리겠습니다.
이순신2022-07-29 17:45:03
기존 ip(10.1.1.12 )는 그대로 사용하고 MAC주소만 변경 요청드립니다. 
문서함  선택없음


"""

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "cli-test":
            parser = Parser()
            parser.parse(test_text)
            print(parser)
    else:
        gui = GuiScreen(version, 400, 600)
        gui.set_parser(Parser())
        gui.open()


