import HTTP from '@/api/common'

const catalogResource = 'real-estates'
const tokenResource = 'jwt'


export const Catalog = {
    getAll () {
        return HTTP.get(`${catalogResource}/`)
    },
    orderByCost (value) {
        return HTTP.get(`${catalogResource}/?ordering=${value}`)
    }
}