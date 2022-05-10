--Change data types for sold
ALTER TABLE sold ALTER COLUMN id TYPE TEXT;

--Change data types for census
ALTER TABLE census ALTER COLUMN tract TYPE TEXT;

--Change data types for tract_crosswalk
ALTER TABLE tract_crosswalk ALTER COLUMN id TYPE TEXT;
ALTER TABLE tract_crosswalk ALTER COLUMN tract TYPE TEXT;

--Join tract_crosswalk table and census table
CREATE TABLE tract_cw_census AS
SELECT
	tract_crosswalk.id,
	tract_crosswalk.tract,
	census.population,
	census.median_income,
	census.pop_w_bach_degree,
	census.same_house_1_year,
	census.moved,
	census.below_100_poverty
FROM
	tract_crosswalk
LEFT JOIN census
	ON tract_crosswalk.tract = census.tract;

--Join sold and tract_cw_census table
CREATE TABLE sold_census AS
SELECT
	sold.id,
	sold.sold_price,
	sold.beds,
	sold.baths,
	sold.area,
	sold.latitude,
	sold.longitude,
	tract_cw_census.population,
	tract_cw_census.median_income,
	tract_cw_census.pop_w_bach_degree,
	tract_cw_census.same_house_1_year,
	tract_cw_census.moved,
	tract_cw_census.below_100_poverty,
	tract_cw_census.tract
FROM
	sold
LEFT JOIN tract_cw_census
	ON sold.id = tract_cw_census.id;

--Calulate distance from each property to approximate center of downtown
Install needed modules;
CREATE EXTENSION CUBE;
CREATE EXTENSION earthdistance;

ALTER TABLE sold_census ADD COLUMN dist_down_town double precision;

UPDATE sold_census SET dist_down_town = (point(longitude,latitude) <@> point(-80.0004,40.4418));
