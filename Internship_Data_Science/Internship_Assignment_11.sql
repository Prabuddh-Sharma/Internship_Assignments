-- Q1. What is the total amount spent by each customer at the restaurant?
-- Sol ->
/*
SELECT
s.customer_id,
SUM(m.price) AS total_spent
FROM
dannys_diner.sales AS s
JOIN
dannys_diner.menu AS m
ON
s.product_id = m.product_id
GROUP BY
s.customer_id;
*/

-- Q2. How many days each customer visited the restaurant?
-- Sol ->
/*
SELECT
s.customer_id,
COUNT(DISTINCT s.order_date) AS Total_Visits 
FROM
dannys_diner.sales AS s
GROUP BY
s.customer_id;
*/

-- Q3. What was the first item from the menu purchased by each customer?
-- Sol ->
/*
SELECT
s.customer_id,
m.product_name,
s.order_date AS First_Visits
FROM
dannys_diner.sales as s
JOIN
dannys_diner.menu as m
ON
s.product_id = m.product_id
WHERE
(s.customer_id, s.order_date)
IN
(SELECT
s.customer_id,
MIN(s.order_date)
FROM
dannys_diner.sales as s
GROUP BY
s.customer_id);
*/

-- Q4. What is the most purchased item on the menu and how many times was it purchased by all customer?
-- Sol ->
/*
SELECT
m.product_name,
t_count.Total_purchase
FROM
(SELECT
s.product_id,
COUNT(s.customer_id) AS Total_purchase
FROM
dannys_diner.sales AS s
GROUP BY
s.product_id
) AS t_count
JOIN
dannys_diner.menu AS m
ON
t_count.product_id = m.product_id
WHERE
t_count.Total_purchase = 
(SELECT
MAX(condi.total_purchase) 
FROM
(SELECT
s.product_id,
COUNT(s.customer_id) AS total_purchase
FROM
dannys_diner.sales AS s
GROUP BY
s.product_id) AS condi);
*/

-- Q5. Which item was the most popular for each customer?
-- Sol ->
/*
select
_items.customer_id,
_items.product_name,
_items.total_per_items
from
(SELECT
s.customer_id,
s.product_id,
m.product_name,
COUNT(s.product_id) AS total_per_items
FROM
dannys_diner.sales AS s
join
dannys_diner.menu as m
on
s.product_id = m.product_id
group by
s.customer_id,
s.product_id,
m.product_name) AS _items
join
(SELECT
customer_id,
MAX(total_per_items) AS max_purchase
FROM
(SELECT
s2.customer_id,
s2.product_id,
COUNT(s2.product_id) AS total_per_items
FROM
dannys_diner.sales AS s2
GROUP BY
s2.customer_id,
s2.product_id) AS all_total_per_items
GROUP BY
customer_id) AS per_cust
ON
_items.customer_id = per_cust.customer_id
AND _items.total_per_items = per_cust.max_purchase;
*/

-- Q6. Which item was purchased first by the customer after they become a member?
-- Sol ->
/*
SELECT
s.customer_id,
m.product_name,
s.order_date AS after_member_date
FROM
dannys_diner.sales AS s
JOIN
dannys_diner.menu AS m
ON 
s.product_id = m.product_id
WHERE (s.customer_id, s.order_date) 
IN 
(SELECT
s.customer_id,
MIN(s.order_date) AS order_date_after_join
FROM
dannys_diner.sales AS s
JOIN
dannys_diner.members AS mem
ON 
s.customer_id = mem.customer_id
WHERE
s.order_date >= mem.join_date
GROUP BY
s.customer_id);
*/

-- Q7. Which item was purchased just before the customer become a member?
-- Sol ->
/*
SELECT
s.customer_id,
m.product_name,
s.order_date AS before_member_date
FROM
dannys_diner.sales AS s
JOIN
dannys_diner.menu AS m
ON 
s.product_id = m.product_id
WHERE (s.customer_id, s.order_date) 
IN 
(SELECT
s2.customer_id,
MAX(s2.order_date) AS order_date_before_join
FROM
dannys_diner.sales AS s2
JOIN
dannys_diner.members AS mem
ON 
s2.customer_id = mem.customer_id
WHERE
s2.order_date < mem.join_date
GROUP BY
s2.customer_id);
*/

-- Q8. What is the total item and amount spent by each member before they become a member? 
-- Sol ->
/*
SELECT
s.customer_id,
COUNT(s.product_id) AS total_items_before,
SUM(m.price) AS total_amount_spent_before
FROM
dannys_diner.sales AS s
JOIN
dannys_diner.members AS mem
ON 
s.customer_id = mem.customer_id
JOIN
dannys_diner.menu AS m
ON 
s.product_id = m.product_id
WHERE
s.order_date < mem.join_date
GROUP BY
s.customer_id;
*/

-- Q9. If each $1 spent equates to 10 points, and sushi has a 2x points multiplier - how many points would each customer have? 
-- Sol. ->
/*
SELECT
s.customer_id,
SUM(CASE
WHEN m.product_name = 'sushi' 
THEN m.price * 10 * 2
ELSE m.price * 10
END) AS total_points
FROM
dannys_diner.sales AS s
JOIN
dannys_diner.menu AS m
ON 
s.product_id = m.product_id
GROUP BY
s.customer_id;
*/

-- Q10. In the first week after a customer joins the program(including their join date), they each earn 2x points on all items, not just sushi. how many points do customer A and B have at the end of January?
-- Sol. ->
/*
WITH customer_points AS (SELECT
s.customer_id,
s.order_date,
m.product_name,
m.price,
mem.join_date,
CASE
WHEN s.order_date >= mem.join_date AND s.order_date < DATE_ADD(mem.join_date, INTERVAL 7 DAY) THEN m.price * 2
ELSE m.price
END AS points_earned
FROM sales AS s
JOIN menu AS m
ON s.product_id = m.product_id
LEFT JOIN members AS mem
ON s.customer_id = mem.customer_id
WHERE s.customer_id IN ('A', 'B') AND s.order_date <= '2021-01-31')
SELECT
customer_id,
SUM(points_earned) AS total_points
FROM customer_points
GROUP BY
customer_id;
*/