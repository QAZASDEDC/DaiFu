@daifu.transform(globals())
def main():
    running_reward = 10
    for i_episode in count(1):
        state, _ = env.reset()
        ep_reward = 0
        for t in range(1, 10000):
            action = select_action(state)
            state, reward, done, _, _ = env.step(action)
            if args.render:
                env.render()
            model.rewards.append(reward)
            ep_reward += reward
            if done:
                break
        running_reward = 0.05 * ep_reward + (1 - 0.05) * running_reward
        finish_episode()
        if i_episode % args.log_interval == 0:
            print('Episode {}\tLast reward: {:.2f}\tAverage reward: {:.2f}'.format(i_episode, ep_reward, running_reward))
        if running_reward > env.spec.reward_threshold:
            print('Solved! Running reward is now {} and the last episode runs to {} time steps!'.format(running_reward, t))
            torch.save(model.state_dict(), 'checkpoints/actor_critic_policy.pt')
            break
