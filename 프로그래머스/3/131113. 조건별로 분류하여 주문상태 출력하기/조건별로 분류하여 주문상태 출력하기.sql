-- 코드를 입력하세요
SELECT ORDER_ID
    , PRODUCT_ID
    , DATE_FORMAT(OUT_DATE,'%Y-%m-%d') AS 'OUT_DATE'
    , CASE 
        WHEN DATE_FORMAT(OUT_DATE,'%Y-%m-%d') > DATE_FORMAT('2022-05-01','%Y-%m-%d') THEN '출고대기'
        WHEN DATE_FORMAT(OUT_DATE,'%Y-%m-%d') <= DATE_FORMAT('2022-05-01','%Y-%m-%d') THEN '출고완료'
        WHEN OUT_DATE IS NULL THEN '출고미정'    
        END AS '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID 