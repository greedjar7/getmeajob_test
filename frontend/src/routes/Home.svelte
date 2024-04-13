default 화면에 대한 설정

<script>
    import fastapi from '../lib/api'
    import { link } from 'svelte-spa-router'

    let cv_list = []

    function get_cv_list() {
        fastapi('get', '/api/get_cv_db/cv_list', {}, (json) => {
            cv_list = json
        })
    }

    get_cv_list()
</script>

<ul>
    {#each cv_list as cv}
        <li><a use:link href="/detail/{cv.id}">{cv.title}</a></li>
    {/each}
</ul>
