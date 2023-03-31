import {useSelector} from 'react-redux';
// проверка авторизации пользователя и возможность узнать его авторизационные данные
export function useAuth() {
    const {email, token, id} = useSelector(state => state.user);

    return {
        isAuth: !!email,
        email,
        token,
        id,
    };
}