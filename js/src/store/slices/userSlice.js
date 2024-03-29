import {createSlice} from '@reduxjs/toolkit';

const initialState = {
    email: null,
    token: null,
    id: null,
};

const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        setUser(state, action) {                        // создание пользователя
            state.email = action.payload.email;
            state.token = action.payload.token;
            state.id = action.payload.id;
        },
        removeUser(state) {                             // удаление пользователя
            state.email = null;
            state.token = null;
            state.id = null;
        },
    },

});

export const {setUser, removeUser} = userSlice.actions;

export default userSlice.reducer;