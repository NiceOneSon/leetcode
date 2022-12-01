-- -- 코드를 입력하세요
SELECT TO_CHAR(SALES_DATE, 'YYYY-MM-DD') AS SALES_DATE
      ,PRODUCT_ID
      ,USER_ID
      ,SALES_AMOUNT
  FROM 
    (
    SELECT SALES_DATE
          ,PRODUCT_ID
          ,USER_ID
          ,SALES_AMOUNT
      FROM ONLINE_SALE
     UNION ALL
    SELECT SALES_DATE
          ,PRODUCT_ID
          ,NULL AS USER_ID
          ,SALES_AMOUNT
      FROM OFFLINE_SALE
    ) A
 WHERE SALES_DATE >= TO_DATE('20220301', 'YYYYMMDD')
   AND SALES_DATE < TO_DATE('20220401', 'YYYYMMDD')
 ORDER BY SALES_DATE, PRODUCT_ID, USER_ID