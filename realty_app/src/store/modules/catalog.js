import {Catalog} from '@/api/catalog'
import {GET_ALL_REAL_ESTATES} from '@/store/mutation-types'

const state = () => ({
    catalog: []
})

const getters = {}

const mutations = {
    [GET_ALL_REAL_ESTATES](state, data) {
        state.catalog = data
    }
}

const actions = {
    getAll({commit}) {
        return Catalog.getAll().then(response => {
            commit(GET_ALL_REAL_ESTATES, response.data)
            return response
        })
    },
    orderByCost({commit} ,value) {
        return Catalog.orderByCost(value).then(response => {
            return response
        })
    }
}

export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
}

