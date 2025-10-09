total_area = 400
interior_cost_per_sq_meter = 1000
exterior_cost_per_sq_meter = 1200
interior_area = total_area * 8
exterior_area = total_area *7
interior_cost = interior_area * interior_cost_per_sq_meter
exterior_cost = exterior_area * exterior_cost_per_sq_meter
total_cost = interior_cost + exterior_cost
print(f'Interior wall area: {interior_area} sq meters')
print(f'Exterior wall area: {exterior_area} sq meters')
print(f'Interior wall cost: {interior_cost}')
print(f'Exterior wall cost: {exterior_cost}')
print(f'Total wall cost: {total_cost}')