USE clique_bait;
-- Q1. How many users are there?
-- Sol ->
/*select
count(1) as total_users
from
users as u;*/

-- Q2. How many cookies does each user have on average?
-- Sol ->
/*
SELECT
SUM(total_cookies) / (SELECT COUNT(DISTINCT user_id) FROM users) AS average_cookies_per_user
FROM
(SELECT
user_id,
COUNT(cookie_id) AS total_cookies
FROM
users AS u
GROUP BY
user_id) AS sum_total_cookie;
*/

-- Q3. What is the unique number of visits by all users per month?
-- Sol ->
/*
select
date_format(event_time, '%Y-%m') as visited_months,
count(distinct visit_id) as unique_visits
from
events as e
group by 
visited_months;
*/

-- Q4. What is the number of events for each event type?
-- Sol ->
/*
select
ei.event_name,
count(*) as total_events
from
events as e
join
event_identifier as ei
on
e.event_type = ei.event_type
group by
ei.event_name;
*/

-- Q5. What is the percentage of visits which have a purchase event?
-- Sol ->
/*
select
cast((select
count(distinct e.visit_id) as unique_
from
event_identifier as ei
join
events as e
on
ei.event_type = e.event_type
where
ei.event_type = 3
) as decimal(10,2)) * 100.0/ 
(select count(distinct visit_id) from events) as percentage_visits_purchase;
*/

-- Q6. What is the percentage of visits which view the checkout page but do not have a purchase event?
-- Sol ->
/*
select 
event_type 
from
event_identifier 
where event_name = 'Purchase';

select
cast(
(select
count(distinct e.visit_id) 
from
events as e
where
e.event_type = 4 and e.visit_id not in 
(select
distinct e.visit_id
from
events as e
where
e.event_type = 3)) as decimal(10,2))/
(select
count(distinct e.visit_id) 
from
events as e 
where 
event_type = 4
) as percentage_checkout;
 */
 
 -- Q7. What are the top 3 pages by number of views?
 -- Sol ->
 /*
select
p.page_name,
COUNT(*) as total_views
from
events as e
join
event_identifier as ei
on
e.event_type = ei.event_type
join
page_hierarchy as p
on
e.page_id = p.page_id
where
ei.event_name = 'Page View'
group by
p.page_name
order by
total_views DESC;
*/

-- Q8. What is the number of views and cart adds for each product category?
-- Sol ->
/*
select
p.product_category,
sum(case 
when ei.event_name = 'Page View' 
then 1 
else 0 
end) as total_views,
sum(case 
when ei.event_name = 'Add to Cart' 
then 1 
else 0 
end) as total_cart_adds
from
events as e
join
event_identifier as ei
on
e.event_type = ei.event_type
join
page_hierarchy as p
on
e.page_id = p.page_id
where
ei.event_name 
IN ('Page View', 'Add to Cart')
group by
p.product_category;
*/

-- Q9. What are the top 3 products by purchases?
-- Sol ->
/*
select
p.page_name as product_name,
count(*) as total_purchases
from
events as e
join
event_identifier as ei
on
e.event_type = ei.event_type
join
page_hierarchy as p
on
e.page_id = p.page_id
where
ei.event_name = 'Purchase'
group by
p.page_name;
*/