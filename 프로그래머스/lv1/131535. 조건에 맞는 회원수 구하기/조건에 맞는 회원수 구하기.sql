-- 코드를 입력하세요
SELECT COUNT(USER_ID) FROM USER_INFO WHERE 20<=AGE AND AGE<= 29 AND SUBSTRING_INDEX(JOINED, '-',1) = '2021';
# SELECT * FROM USER_INFO; 
# 2021 총 158명