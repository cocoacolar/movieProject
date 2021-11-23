<template>
  <li class="media">
    <div class="media-left">
        <a href="#x">
            <img class="media-object" alt="" src="images/creator.jpg">
        </a>
    </div>
    <div class="media-body">
        <div class="comment-info">
            <div class="comment-date text-sm"><i class="far fa-clock mr-1"></i> {{ comment.updated_at }}</div>
            <div class="comment-author"><a href="#x"><b>{{ comment.id }}</b></a></div>
        </div><!-- / comment-info -->
        <div class="comment">
            <p class="mb-0">{{ comment.content }}</p>
        </div><!-- / comment -->

        <!-- nested media objects -->
        
    </div><!-- / parent media-body -->
  </li><!-- / media -->
</template>

<script>
export default {
  name: 'MovieDetailCommentItem',
  props: {
    comment: {
      type: Object,
    }
  },
}
</script>

<style>

</style>