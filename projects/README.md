# 03_db 

### 01_create_table.sql

```sql
-- 테이블 생성
CREATE TABLE movies (
    '영화코드' INTEGER PRIMARY KEY,
    '영화이름' TEXT,
    '관람등급' TEXT,
    '감독' TEXT,
    '개봉연도' DATE,
    '누적관객수' INTEGER,
    '상영시간' INTEGER,
    '제작국가' TEXT,
    '장르' TEXT
);
-- import boxoffice csv
.mode csv
.import boxoffice.csv movies

.headers on
.mode column

SELECT * FROM movies;
```



### 02_crud.sql

```sql
--영화를 테이블에 추가
INSERT INTO moveis('영화코드','영화이름','관람등급','감독','개봉연도','누적관객수','상영시간','제작국가','장르')
VALUES(20182530, '극한직업', '15세이상관람가', '이병헌', 20190123, 3138467, 111, '한국', '코미디');

--영화코드가 20040521dls 영화를 찾아서 삭제
SELECT*FROM movies WHERE 영화코드=20040521;
DELETE FROM movies WHERE 영화코드=20040521;

--영화코드가 20185124인 영화를 찾아서 공백에 '없음'을 추가
SELECT*FROM movies WHERE 영화코드=20185124;
UPDATE movies 
SET 영화감독='없음'
WHERE  영화코드=20185124;
```



### 03_select.sql

```sql
--상영시간이 150분이상인 영화이름 찾기
SELECT 영화이름 FROM movies WHERE 상영시간>=150;

--장르가 애니메이션인 영화코드,영화이름 찾기
SELECT 영화코드,영화이름 FROM movies WHERE 장르="애니메이션";

--제작국가가 덴마크이고 장르가 애니메이션인 영화이름 찾기
SELECT 영화이름 FROM movies WHERE 제작국가="덴마크" and 장르="애니메이션";

--누적관객수가 100만이상이고 관람등급이 청소년이상인 영화이름과 누적관객수 찾기
SELECT 영화이름, 누적관객수 FROM movies WHERE 누적관객수>1000000 and 관람등급="청소년관람불가";

--LIKE를 사용하여 2000-2009년 개봉연도 영화 찾기
SELECT*FROM movies WHERE 개봉연도 LIKE '200%';

--DISTINCT를 사용하여 중복없이 장르 찾기
SELECT DISTINCT 장르 FROM movies;
```



### 04_expression.sql

```sql
--SUM()를 사용하여 총누적관객수 찾기
SELECT SUM(누적관객수) FROM movies;

--MAX()를 사용하여 가장 많은 누적관객수인 영화이름과 누적관객수 찾기
SELECT 영화이름,MAX(누적관객수) FROM movies;

--MIN()을 사용하여 가장 짧은 상영시간 장르와 상영시간 찾기
SELECT 장르,MIN(상영시간) FROM movies;

--AVG()를 사용하여 평균값구하여 찾기
SELECT AVG(누적관객수) FROM movies WHERE 제작국가="한국";

--COUNT()를 사용하여 개수 찾기
SELECT COUNT(*) FROM movies WHERE 관람등급="청소년관람불가";

SELECT COUNT(*) FROM movies WHERE 상영시간>=100 and 장르="애니메이션";
```



### 05_order.sql

```sql
--ORDER BY DESC(내림차순),ASC(오름차순) LIMIT [원하는 출력개수] 사용하여 찾기
SELECT*FROM movies ORDER BY 누적관객수 DESC LIMIT 5;

SELECT*FROM movies WHERE 장르="애니메이션"
ORDER BY 제작국가 ASC, 누적관객수 DESC LIMIT 10;

SELECT 감독 FROM movies ORDER BY 상영시간 DESC LIMIT 10;
```

