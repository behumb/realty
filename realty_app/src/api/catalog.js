import HTTP from '@/api/common'

const catalogResource = 'real-estates'
const tokenResource = 'jwt'


export const Catalog = {
    getAll() {
        return HTTP.get(`${catalogResource}/`)
    },
    orderByCost(value) {
        return HTTP.get(`${catalogResource}/?ordering=${value}`)
    },
    filter(data) {
        const filterString = `?ordering=${data['ordering']}&property_type__name=${data['property_type']}&location__city=${data['city']}&min_price=${data['min_price']}&max_price=${data['max_price']}&min_square=${data['min_square']}&max_square=${data['max_square']}&bedrooms=${data['bedrooms']}&bathroom=${data['bathrooms']}`
        return HTTP.get(`${catalogResource}/${filterString}`)
    }
}