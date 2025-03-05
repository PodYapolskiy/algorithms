select distinct
    v.customer_id, count(v.customer_id) as count_no_trans
from
    visits as v
where
    v.visit_id not in (
        select distinct
            t.visit_id
        from
            transactions as t
    )
group by
    v.customer_id