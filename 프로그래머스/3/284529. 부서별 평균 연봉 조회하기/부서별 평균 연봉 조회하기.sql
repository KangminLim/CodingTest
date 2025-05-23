-- 코드를 작성해주세요
SELECT B.DEPT_ID, A.DEPT_NAME_EN, ROUND(SUM(B.SAL)/COUNT(B.DEPT_ID)) AS AVG_SAL 
# SELECT *
FROM HR_DEPARTMENT AS A INNER JOIN 
    HR_EMPLOYEES AS B ON A.DEPT_ID = B.DEPT_ID
GROUP BY DEPT_ID 
ORDER BY AVG_SAL DESC