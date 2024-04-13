<script>
    import fastapi from '../lib/api'

    export let params = {}
    let cv_id = params.cv_id
    
    let cv = {}

    function get_cv() {
        fastapi('get', '/api/get_cv_db/detail/' + cv_id, {}, (json) => {
            cv = json
        })
    }

    get_cv()
</script>

<h1>{'회사명: '}{cv.company}</h1>
<div>
    {'공고 제목: '}{cv.title}<br>
    {'채용 상세 사항: '}{cv.detail}<br>
    {'채용 링크: '}{cv.href}
</div>
