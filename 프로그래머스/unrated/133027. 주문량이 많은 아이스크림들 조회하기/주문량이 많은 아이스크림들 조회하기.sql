-- 코드를 입력하세요
SELECT A.FLAVOR
  FROM 
    (SELECT A.FLAVOR, RANK() OVER(ORDER BY A.TOTAL_ORDER + B.TOTAL_ORDER DESC) AS RNK
      FROM  (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
               FROM FIRST_HALF
              GROUP BY FLAVOR) A,
            (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
               FROM JULY
              GROUP BY FLAVOR) B
     WHERE A.FLAVOR = B.FLAVOR
    ) A
 WHERE RNK <= 3