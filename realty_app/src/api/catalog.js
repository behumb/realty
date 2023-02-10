import HTTP from '@/api/common'

const catalogResource = 'real-estates'
const tokenResource = 'jwt'


export const Catalog = {
    getAll () {
        return HTTP.get(`${catalogResource}/`)
    }
}